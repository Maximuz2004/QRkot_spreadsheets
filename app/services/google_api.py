from copy import deepcopy
from datetime import datetime, timedelta

from aiogoogle import Aiogoogle

from app.core.config import settings

FORMAT = '%Y/%m/%d %H:%M:%S'
SHEET_TITLE = 'Отчет на {}'
SPREADSHEET_BODY = dict(
    properties=dict(title='', locale='ru_RU'),
    sheets=[dict(properties=dict(
        sheetType='GRID',
        sheetId=0,
        title='Лист1',
        gridProperties=dict(rowCount=100, columnCount=11)
    ))]
)
PERMISSION_USER_DATA = dict(
    type='user',
    role='writer',
    emailAddress=settings.email
)
PERMISSION_FIELD = 'id'
DRIVE_API_NAME = 'drive'
DRIVE_API_VERSION = 'v3'
SHEETS_API_NAME = 'sheets'
SHEETS_API_VERSION = 'v4'
TABLE_VALUES = [
    ['Отчет от', ''],
    ['Топ проектов по скорости закрытия'],
    ['Название проекта', 'Время сбора', 'Описание']
]
RANGE = 'A1:E{}'
VALUE_INPUT_OPTION = 'USER_ENTERED'
MAJOR_DIMENSION = 'ROWS'


async def spreadsheets_create(wrapper_services: Aiogoogle) -> str:
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
    return response['spreadsheetId']


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
            fields=PERMISSION_FIELD
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
    for project in projects:
        new_row = [
            project.name,
            str(timedelta(project.date_difference)),
            project.description
        ]
        table_values.append(new_row)
        await wrapper_services.as_service_account(
            service.spreadsheets.values.update(
                spreadsheetId=spreadsheet_id,
                range=RANGE.format(len(table_values)),
                valueInputOption=VALUE_INPUT_OPTION,
                json={
                    'majorDimension': MAJOR_DIMENSION,
                    'values': table_values
                }
            )
        )
