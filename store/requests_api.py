from django_project.external_service import ConnectService


def get_subcategory_attrs(params: dict):
    return ConnectService.service(
        method="GET",
        url="/url/",
        params=params,
    )
