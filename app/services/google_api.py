from copy import deepcopy
from datetime import datetime, timedelta

from aiogoogle import Aiogoogle

from app.core.config import settings

FORMAT = '%Y/%m/%d %H:%M:%S'
SHEET_TITLE = 'Отчет на {}'
ROW_COUNT = 100
COLUMN_COUNT = 11
SHEET_ERROR_MESSAGE = (f'Передана некорректная информация. Ожидалось '
                       f'{ROW_COUNT} строк и {COLUMN_COUNT} колонок. '
                       'Передано {} строк и {} колонок.')
SPREADSHEET_BODY = dict(
    properties=dict(title='', locale='ru_RU'),
    sheets=[dict(properties=dict(
        sheetType='GRID',
        sheetId=0,
        title='Лист1',
        gridProperties=dict(rowCount=ROW_COUNT, columnCount=COLUMN_COUNT)
    ))]
)
PERMISSION_USER_DATA = dict(
    type='user',
    role='writer',
    emailAddress=settings.email
)
DRIVE_API_NAME = 'drive'
DRIVE_API_VERSION = 'v3'
SHEETS_API_NAME = 'sheets'
SHEETS_API_VERSION = 'v4'
TABLE_VALUES = [
    ['Отчет от', ''],
    ['Топ проектов по скорости закрытия'],
    ['Название проекта', 'Время сбора', 'Описание']
]
RANGE = 'R1C1:R{}C{}'
VALUE_INPUT_OPTION = 'USER_ENTERED'
MAJOR_DIMENSION = 'ROWS'


async def spreadsheets_create(wrapper_services: Aiogoogle) -> dict:
    service = await wrapper_services.discover(
        SHEETS_API_NAME,
        SHEETS_API_VERSION
    )
    spreadsheet_body = deepcopy(SPREADSHEET_BODY)
    spreadsheet_body['properties']['title'] = SHEET_TITLE.format(
        datetime.now().strftime(FORMAT)
    )
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=spreadsheet_body)
    )
    return dict(
        spreadsheet_id=response['spreadsheetId'],
        spreadsheet_url=response['spreadsheetUrl']
    )


async def set_user_permissions(
        spreadsheet_id: str,
        wrapper_services: Aiogoogle,
) -> None:
    service = await wrapper_services.discover(
        DRIVE_API_NAME,
        DRIVE_API_VERSION
    )
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheet_id,
            json=PERMISSION_USER_DATA,
            fields='id'
        )
    )


async def spreadsheets_update_value(
        spreadsheet_id: str,
        projects: list,
        wrapper_services: Aiogoogle,
) -> None:
    service = await wrapper_services.discover(
        SHEETS_API_NAME,
        SHEETS_API_VERSION
    )
    table_values = deepcopy(TABLE_VALUES)
    table_values[0][1] = datetime.now().strftime(FORMAT)
    table_values = [
        *table_values,
        *[[
            project.name,
            str(timedelta(project.date_difference)),
            project.description
        ] for project in projects]
    ]
    row_amount = len(table_values)
    column_amount = max(len(row) for row in table_values)
    if row_amount > ROW_COUNT or column_amount > COLUMN_COUNT:
        raise ValueError(SHEET_ERROR_MESSAGE.format(row_amount, column_amount))
    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheet_id,
            range=RANGE.format(row_amount, column_amount),
            valueInputOption=VALUE_INPUT_OPTION,
            json={
                'majorDimension': MAJOR_DIMENSION,
                'values': table_values
            }
        )
    )
