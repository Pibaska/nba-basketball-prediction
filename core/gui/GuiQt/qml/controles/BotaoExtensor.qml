import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15

Button{
    id: btnExtensor

    //efeitos de cor BotaoExtensor
    property url btnIconeSource: "../../imagens/svg_imagens/expande.png"
    property color btnCorDefault: "#2e2626"
    property color btnCorMouseHover: "#1e1919"
    property color btnCorClique: "#3e3333"

    QtObject{
        id: internal

        property var dynamicColor: if(btnExtensor.down){
                                      btnExtensor.down ? btnCorClique : btnCorDefault
                                   } else{
                                       btnExtensor.hovered ? btnCorMouseHover : btnCorDefault
                                   }
    }




    implicitWidth: 70
    implicitHeight: 60

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
        height: 25
        width: 25

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
    D{i:0;formeditorZoom:1.66}
}
##^##*/
