import reflex as rx


class OrganizationList(rx.Component):
    library = "@clerk/clerk-react"
    tag = "OrganizationList"


organization_list = OrganizationList.create
