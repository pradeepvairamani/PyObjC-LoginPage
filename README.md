
  1. Create a new view (Xib)
  2. Add the python file with the @objc.IBAction and objc.IBOutlet()
  3. Click on file owner is Xcode and Identity Inspector.
  4. Change class name to the class of the class that inherits NSWindowController
  5. In connection inspector we should see the methods of .py file and drag these onto the appropriate buttons or textfields
  6. py2applet --make-setup <app name>.py to generate the setup.py
  7. Add the xib to setup.py and run python setup.py py2app.
  8. The dist directory will have the executable that we need.
