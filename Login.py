# from Cocoa import *
from AppKit import NSWindowController, NSApplication, NSApp
from Cocoa import objc


class SimpleXibDemoController(NSWindowController):
    counterTextField = objc.IBOutlet()
    username_field = objc.IBOutlet()
    password_field = objc.IBOutlet()

    def windowDidLoad(self):
        NSWindowController.windowDidLoad(self)

    @objc.IBAction
    def submit_(self, sender):
        username = self.username_field.stringValue()
        password = self.password_field.stringValue()
        self.updateDisplay(username+' '+password)

    def updateDisplay(self, value):
        self.counterTextField.setStringValue_(value)

    def get_input(self):
        return self.username_field.stringValue()

if __name__ == "__main__":
    app = NSApplication.sharedApplication()

    # Initiate the contrller with a XIB
    viewController = SimpleXibDemoController.alloc().initWithWindowNibName_("Login")

    # Show the window
    viewController.showWindow_(viewController)

    # Bring app to top
    NSApp.activateIgnoringOtherApps_(True)

    from PyObjCTools import AppHelper
    AppHelper.runEventLoop()
