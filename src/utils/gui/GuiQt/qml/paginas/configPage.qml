import QtQuick 2.0
import QtQuick.Controls 2.15
import "../controles"

Item {
    Rectangle {
        id: rectangle
        color: "#1d1d1d"
        anchors.fill: parent

        Label {
            id: label
            x: 387
            y: 234
            color: "#ffffff"
            text: qsTr("Config")
            anchors.verticalCenter: parent.verticalCenter
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            font.pointSize: 20
            anchors.horizontalCenter: parent.horizontalCenter
        }








    }

}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
##^##*/
