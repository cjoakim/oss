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
    @FXML private Label            computerUserIdLabel;
    @FXML private Label            webAppUserIdLabel;
    @FXML private Label            webEnvironmentLabel;
    @FXML private Button           walkFilesBtn;
    @FXML private Button           parseSelectedBtn;
    @FXML private Button           parseAllBtn;
    @FXML private Button           getWebMetadataBtn;
    @FXML private Button           postSelectedBtn;
    @FXML private Button           postAllBtn;
    @FXML private TabPane          mainTabPane;
    @FXML private Tab              partsListTab;
    @FXML private TableView        partsTableView;
    @FXML private TableColumn      partsTableViewSeq;
    @FXML private TableColumn      partsTableViewDiff;
    @FXML private TableColumn      partsTableViewDup;
    @FXML private TableColumn      partsTableViewCommon;
    @FXML private TableColumn      partsTableViewPartname;
    @FXML private TableColumn      partsTableViewFilename;
    @FXML private TableColumn      partsTableViewModDate;
    @FXML private Tab              partDetailsTab;
    @FXML private TextField        detailFilenameTF;
    @FXML private TextField        detailLocPartnameTF;
    @FXML private TextField        detailWebPartnameTF;
    @FXML private TextField        detailLocFilesizeTF;
    @FXML private TextField        detailWebFilesizeTF;
    @FXML private TextField        detailLocCommonTF;
    @FXML private TextField        detailWebCommonTF;
    @FXML private TextField        detailLocTvSizesTF;
    @FXML private TextField        detailWebTvSizesTF;
    @FXML private TextField        detailLocModTimeTF;
    @FXML private TextField        detailWebModTimeTF;
    @FXML private Tab              configurationTab;
    @FXML private Text             readOnlyGroupText;
    @FXML private TextField        nodeLocationTF;
    @FXML private TextField        appLocationTF;
    @FXML private TextField        drawingsLocationTF;
    @FXML private TextField        webProductionUrlTF;
    @FXML private TextField        webStagingUrlTF;
    @FXML private TextField        webLocalUrlTF;
    @FXML private Text             userEditableGroupText;
    @FXML private ComboBox         webEnvironmentsOldnameCbox;
    @FXML private TextField        webAppUserIdTF;
    @FXML private TextField        webAppPasswordTF;
    @FXML private Button           saveWebCredentialsBtn;
    @FXML private Button           testLogonBtn;
    @FXML private Label            statusMessageLabel;

    // UI Event Handler methods:

    @FXML public void walkFilesBtnClicked(ActionEvent e) {

    }

    @FXML public void parseSelectedBtnClicked(ActionEvent e) {

    }

    @FXML public void parseAllBtnClicked(ActionEvent e) {

    }

    @FXML public void getWebMetadataBtnClicked(ActionEvent e) {

    }

    @FXML public void postSelectedBtnClicked(ActionEvent e) {

    }

    @FXML public void partsTableViewClicked(ActionEvent e) {

    }

    @FXML public void webEnvironmentSelected(ActionEvent e) {

    }

    @FXML public void saveWebCredentialsBtnClicked(ActionEvent e) {

    }

    @FXML public void testLogonBtnClicked(ActionEvent e) {

    }

}
