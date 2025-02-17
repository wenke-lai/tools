import reflex as rx


class OrganizationSwitcher(rx.Component):
    library = "@clerk/clerk-react"
    tag = "OrganizationSwitcher"


organization_switcher = OrganizationSwitcher.create
