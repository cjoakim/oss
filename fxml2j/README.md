## fxml2j

### Purpose

This library is for generating code for JavaFX applications which use FXML for UI layout.

While FXML is a clean and convenient format for representing the UI layout of the application,
current tooling (i.e. - SceneBuilder, et al) do not allow you to synchronize the FXML code
to the underlying JavaFX Controller code.  The underlying Java code can be quite verbose,
and is tedious to manually write.

The 'fxml2j' library will BOTH generate an implementation of the Java Controller class,
as well as show you ongoing "diffs" between your FXML and Controller class as each of these
two code artifacts evolves.  The library will discover the fx:id elements, and #-prefixed
action methods, and generate the appropriate @FXML annotated Java code.

### Examples

#### Setup

Add fxml2j to your project or package.json file:
```
npm install fxml2j
```

Require fxml2j in your code:
```
Fxml2j  = require("fxml2j").Fxml2j
```

Create your 'fxml2j.json' configuration file, for example:
```
{
  "javafx_src_dir": "workspace/ExampleApp/src",
  "fxml_filename":  "com/joakim/example/Example.fxml",

  "generate": true,
  "diff":     true,
  "verbose":  true,

  "multiWordTagMappings": {
    "borderpane":    "BorderPane",
    "combobox":      "ComboBox",
    "gridpane":      "GridPane",
    "tablecolumn":   "TableColumn",
    "tableview":     "TableView",
    "tabpane":       "TabPane",
    "textfield":     "TextField",
    "addadditional": "AddAdditional"
  }
}
```

Alternatively, rather than reading a JSON file, construct a similar configuration object
in your code to pass to Fxml2j.

The 'javafx_src_dir' property should point to the root source directory of your
JavaFX codebase.  This examples shows an Eclipse workspace location.

The 'fxml_filename' property points to your main FXML file relative to the 'javafx_src_dir'.
The current version of fxml2j does not handle fx:include tags, but this will be added
in a future release.  The Example.fxml is in this GitHub repository.

Only one Controller class is currently supported by fxml2j.  This classname is obtained by
parsing the FXML and identifying the 'fx:controller'.  The generated controller code is
written as a *.txt file in the controller directory - see example output filenames below.
This is so that it does not overlay the current corresponding *.java file.

Note: this library is implemented with CoffeeScript, and these examples are also in CoffeeScript.

#### Fxml2j

Using the fxml2j library:

``` 
Fxml2j = require("./lib/fxml2j.js").Fxml2j

config_json = fs.readFileSync('fxml2j.json', 'utf-8')
config_obj  = JSON.parse(config_json)

fxml = new Fxml2j(config_obj)
fxml.process()
```

Example output from the above CoffeeScript code is shown below.

Notice that the differences between the FXML and the correspondingare Java Controller
class are identified.  The fxml2j library currently requires, for ease of parsing,
that your @FXML annotations are "inlined" into your variable and method declaration lines.

```
fxml parsed; controller: com.joakim.example.ExampleController  ui components: 50
controller_package:   com.joakim.example
controller_classname: ExampleController
controller_filename:  workspace/ExampleApp/src/com/joakim/example/ExampleController.java
file written:         workspace/ExampleApp/src/com/joakim/example/ExampleController.txt
the controller file currently exists, line count: 103

Differences - Add - 10
    @FXML private Label            osNameLabel;
    @FXML private Label            buildTimestampLabel;
    @FXML private TableColumn      partsTableViewFilesize;
    @FXML private ComboBox         webEnvironmentsCbox;
    @FXML public void postAllBtnClicked(ActionEvent e) {
    @FXML private Label            osNameLabel;
    @FXML private Label            buildTimestampLabel;
    @FXML private TableColumn      partsTableViewFilesize;
    @FXML private ComboBox         webEnvironmentsCbox;
    @FXML public void postAllBtnClicked(ActionEvent e) {
Differences - Delete - 1
    @FXML private ComboBox         webEnvironmentsOldnameCbox;
```

Example FXML code.  The 'fx:controller' and 'fx:id' components are parsed by fxml2j,
as are the onXxxx="#xxx" event handler method names.

```
...

<BorderPane maxHeight="-Infinity" maxWidth="-Infinity"
  minHeight="-Infinity" minWidth="-Infinity" prefHeight="650.0"
  prefWidth="1200.0" xmlns="http://javafx.com/javafx/8" xmlns:fx="http://javafx.com/fxml/1"
  fx:controller="com.joakim.example.ExampleController" >

...

        <Button fx:id="postSelectedBtn" mnemonicParsing="false" prefWidth="200.0"
          onAction="#postSelectedBtnClicked" text="Post Selected" />
        <Label text=" " />

...

```

Example Generated Java code:

```

package com.joakim.example;

import javafx.scene.control.BorderPane;
import javafx.scene.control.Button;
import javafx.scene.control.ComboBox;
import javafx.scene.control.Label;
import javafx.scene.control.Tab;
import javafx.scene.control.TabPane;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.Text;
import javafx.scene.control.TextField;

public class ExampleController {

    // Instance variables - fx:id UI components:
    
    ...
    
    @FXML private Button           postSelectedBtn;


    ...

    @FXML public void postSelectedBtnClicked(ActionEvent e) {

    }

    ...
}
```

With these diffs identified, the intent is for you to copy-and-paste the Added code
into your controller, while manually deleting the identified Deletions.  In cases
where the Controller class does not exist, simply rename the generated "*.txt" file
to "*.java".


### Release History

* 2015-03-03   v0.1.2  Fixed main in package.json
* 2015-02-24   v0.1.1  README updated with example FXML and Java code
* 2015-02-22   v0.1.0  initial working version
