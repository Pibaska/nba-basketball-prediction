import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15

Button{
    id: btnTopBar

    //efeitos de cor btnTopBar
    property url btnIconeSource: "../../imagens/svg_imagens/minimizar.png"
    property color btnCorDefault: "#2e2626"
    property color btnCorMouseHover: "#1e1919"
    property color btnCorClique: "#3e3333"

    QtObject{
        id: internal

        property var dynamicColor: if(btnTopBar.down){
                                      btnTopBar.down ? btnCorClique : btnCorDefault
                                   } else{
                                       btnTopBar.hovered ? btnCorMouseHover : btnCorDefault
                                   }
    }




    implicitWidth: 35
    implicitHeight: 35

    background: Rectangle{
        id:bgBtn
        color: internal.dynamicColor
    }

    Image{
        id: iconeBtn
        source: btnIconeSource
        fillMode: Image.PreserveAspectFit
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter
        height: 16
        width: 16

    }

    ColorOverlay{
        anchors.fill: iconeBtn
        source: iconeBtn
        color: "#ffffff"
        antialiasing: false
    }


}


/*##^##
Designer {
    D{i:0;formeditorZoom:4}
}
##^##*/
