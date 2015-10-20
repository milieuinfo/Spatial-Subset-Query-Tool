# -*- coding: utf-8 -*-
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt4.QtGui import QAction, QIcon
from vmmQry_dialog import vmmQryDialog
from settingsDlg import settingsDlg
import os.path


class vmmQry:
    def __init__(self, iface):
        """Constructor.
        
        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale", "en")[0:2] 
        if not locale in ['en','nl'] : locale = 'en'

        locale_path = os.path.join(
            self.plugin_dir, 'i18n', '{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)
        
        # Create the dialog (after translation) and keep reference
        self.vmmQryDlg = vmmQryDialog(self.iface, self.iface.mainWindow() )
        self.settingsDlg = settingsDlg(self.iface, self.iface.mainWindow())

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Spatial Subset Query tool')
        self.toolbar = self.iface.addToolBar(u'vmmQry')
        self.toolbar.setObjectName(u'vmmQry')

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('vmmQry', message)

    def add_action( self, icon_path,  text, callback, enabled_flag=True,  add_to_menu=True, add_to_toolbar=True, status_tip=None, parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToDatabaseMenu( self.menu, action)

        self.actions.append(action)

        return action

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Spatial Subset Query tool'), action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""
        self.add_action(
            ':/plugins/vmmQry/images/Sql-icon.png',
            text=self.tr(u'Query Subset op intersectie'),
            callback=self.runVmmQryDlg,
            parent=self.iface.mainWindow())
        self.add_action(
            ':/plugins/vmmQry/images/settings.png',
            text=self.tr(u'Instellingen'),
            callback=self.runSettingsDlg,
            parent=self.iface.mainWindow())

    def runSettingsDlg(self):
        ' show the settings dialog'
        if self.vmmQryDlg.isVisible():
           self.vmmQryDlg.showNormal()
           self.vmmQryDlg.activateWindow()
           return

        self.settingsDlg.setup()
        self.settingsDlg.show()
        # Run the dialog event loop
        result = self.settingsDlg.exec_()
        # See if OK was pressed
        if result:
           self.vmmQryDlg.setup()

    def runVmmQryDlg(self):
        ' show the base dialog'
        if self.vmmQryDlg.isVisible():
           self.vmmQryDlg.showNormal()
           self.vmmQryDlg.activateWindow()
           return
        self.vmmQryDlg.show()
        # Run the dialog event loop
        result = self.vmmQryDlg.exec_()
        # See if OK was pressed
        if result:
            pass
