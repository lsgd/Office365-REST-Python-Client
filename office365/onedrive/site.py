from office365.onedrive.baseItem import BaseItem
from office365.runtime.resource_path import ResourcePath
from office365.onedrive.columnDefinitionCollection import ColumnDefinitionCollection
from office365.onedrive.contentTypeCollection import ContentTypeCollection
from office365.onedrive.drive import Drive
from office365.onedrive.driveCollection import DriveCollection
from office365.onedrive.listCollection import ListCollection


class Site(BaseItem):
    """The site resource provides metadata and relationships for a SharePoint site. """

    @property
    def columns(self):
        """The collection of columns under this site."""
        if self.is_property_available('columns'):
            return self.properties['columns']
        else:
            return ColumnDefinitionCollection(self.context,
                                              ResourcePath("columns", self.resourcePath))

    @property
    def contentTypes(self):
        """The collection of content types under this site."""
        if self.is_property_available('contentTypes'):
            return self.properties['contentTypes']
        else:
            return ContentTypeCollection(self.context,
                                         ResourcePath("contentTypes", self.resourcePath))

    @property
    def lists(self):
        """The collection of lists under this site."""
        if self.is_property_available('lists'):
            return self.properties['lists']
        else:
            return ListCollection(self.context, ResourcePath("lists", self.resourcePath))

    @property
    def drive(self):
        """The default drive (document library) for this site."""
        if self.is_property_available('drive'):
            return self.properties['drive']
        else:
            return Drive(self.context, ResourcePath("drive", self.resourcePath))

    @property
    def drives(self):
        """The collection of drives under this site."""
        if self.is_property_available('drives'):
            return self.properties['drives']
        else:
            return DriveCollection(self.context, ResourcePath("drives", self.resourcePath))

    @property
    def sharepointids(self):
        """Returns identifiers useful for SharePoint REST compatibility."""
        if self.is_property_available("sharepointIds"):
            return self.properties['sharepointIds']
        return None

    @property
    def sites(self):
        """The collection of sites under this site."""
        if self.is_property_available('sites'):
            return self.properties['sites']
        else:
            from office365.onedrive.siteCollection import SiteCollection
            return SiteCollection(self.context,
                                  ResourcePath("sites", self.resourcePath))
