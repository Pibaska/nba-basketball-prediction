import QtQuick 2.0
import QtQuick.Controls 2.15
import "../controles"
import QtQuick.Layouts 1.0
import QtQuick.Controls.Styles 1.4

Item {
    id: item1

    BackgroundChange{

    }

    Rectangle {
        id: rectangle
        color: "#00000000"
        anchors.verticalCenter: parent.verticalCenter
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        clip: false
        anchors.rightMargin: 0
        anchors.leftMargin: 0

        ComboBox {
            id: cbT1
            x: 94
            y: 220
            width: 200
            anchors.verticalCenter: parent.verticalCenter
            anchors.right: image.left
            anchors.rightMargin: 31
            model: [ qsTr("Equipment1"), qsTr("Equipment2"), qsTr("Equipment3"), qsTr("Equipment4"), qsTr("Equipment5"), qsTr("Equipment6") ]
            background: Rectangle{
                color: "#ff5b0f"
                radius: 10
            }




        }

        ComboBox {
            id: cbT2
            y: 220
            width: 200
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: image.right
            anchors.leftMargin: 31
            model: [ qsTr("Equipment1"), qsTr("Equipment2"), qsTr("Equipment3"), qsTr("Equipment4"), qsTr("Equipment5"), qsTr("Equipment6") ]
            background: Rectangle{
                color: "#ff5b0f"
                radius: 10
            }

        }

        Rectangle {
            id: desc
            x: 300
            y: 25
            width: 700
            height: 121
            opacity: 0.8
            color: "#1d1d1d"
            anchors.bottom: image.top
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.bottomMargin: 19
            radius: 15
        }

        Rectangle {
            id: results
            x: 300
            width: 700
            height: 75
            opacity: 0.8
            color: "#1d1d1d"
            anchors.top: image.bottom
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.topMargin: 73
            radius: 15
        }

        BotaoCustom{
            id: btPrever
            x: 300
            text: "Prever!"
            anchors.top: image.bottom
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.topMargin: 17

         }

        Image {
            id: image
            x: 325
            y: 165
            width: 150
            height: 150
            z: 1
            anchors.verticalCenter: parent.verticalCenter
            source: "../../imagens/svg_imagens/bg2.png"
            anchors.horizontalCenter: parent.horizontalCenter
            fillMode: Image.PreserveAspectFit
        }

        Rectangle {
            id: bgimg
            x: 320
            y: 160
            width: 150
            height: 150
            opacity: 0.8
            radius: 75
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            color: "#1d1d1d"
        }


    }


}

/*##^##
Designer {
    D{i:0;autoSize:true;formeditorZoom:0.75;height:480;width:800}
}
##^##*/
