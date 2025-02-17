import reflex as rx


class OrganizationProfile(rx.Component):
    library = "@clerk/clerk-react"
    tag = "OrganizationProfile"


organization_profile = OrganizationProfile.create
