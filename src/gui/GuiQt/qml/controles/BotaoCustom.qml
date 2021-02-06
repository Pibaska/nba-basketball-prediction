import QtQuick 2.15
import QtQuick.Controls 2.15

Button{
    id:customBtn

    //propriedades de cor do botão
    property  color colorDefault: "#232323"
    property  color colorMouseEmCima: "#131313"
    property  color colorClique: "#000000"

    QtObject{
        id: internal

        property var dynamicColor: if(customBtn.down){
                                       customBtn.down ? colorClique : colorDefault
                                   } else{
                                       customBtn.hovered ? colorMouseEmCima : colorDefault
                                   }
    }


    text: qsTr("Botao top")
    implicitWidth: 200
    implicitHeight: 40


    background: Rectangle{
        color: internal.dynamicColor
        radius: 20
        border.color: "#ff8027"
        border.width: 2

    }
    contentItem: Item{
        Text {
            id: textBtn
            text: customBtn.text
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            color: "#ff8027"
        }
    }
}


/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
##^##*/
