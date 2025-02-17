import reflex as rx


class CreateOrganization(rx.Component):
    library = "@clerk/clerk-react"
    tag = "CreateOrganization"


create_organization = CreateOrganization.create
