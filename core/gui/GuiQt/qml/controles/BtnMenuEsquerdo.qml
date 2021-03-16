import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15

Button{
    id: btnMenuEsquerdo
    text: qsTr("Prever!")

    //efeitos de cor BotaoExtensor
    property url btnIconeSourc: "../../imagens/svg_imagens/boladecristal.png"
    property color btnCorDefault: "#2e2626"
    property color btnCorMouseHover: "#1e1919"
    property color btnCorClique: "#3e3333"
    property int iconWidth: 30
    property int iconHeigth: 30
    property color activeMenuColor: "#1d1d1d"
    property color activeMenuColorDireita: "#1d1d1d"
    property bool menuEstaAtivo: true

    QtObject{
        id: internal

        property var dynamicColor: if(btnMenuEsquerdo.down){
                                      btnMenuEsquerdo.down ? btnCorClique : btnCorDefault
                                   } else{
                                       btnMenuEsquerdo.hovered ? btnCorMouseHover : btnCorDefault
                                   }
    }




    implicitWidth: 250
    implicitHeight: 60


    background: Rectangle{
        id:bgBtn
        color: internal.dynamicColor


        Rectangle{
            anchors{
                top: parent.top
                left: parent.left
                bottom: parent.bottom
            }
            color: activeMenuColor
            width: 3
            visible: menuEstaAtivo
        }
        Rectangle{
            anchors{
                top: parent.top
                right: parent.right
                bottom: parent.bottom
            }
            width: 5
            visible: menuEstaAtivo
            color: "#00000000"
        }


    }


    contentItem: Item{
        anchors.fill: parent
        id: content


        Image{
            id: iconeBtn
            source: btnIconeSourc
            anchors.leftMargin: 20
            fillMode: Image.PreserveAspectFit
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: parent.left
            sourceSize.width: iconWidth
            sourceSize.height: iconHeigth
            height: iconHeigth
            width: iconWidth
            antialiasing: true
            visible: true


        }


        Text {
            id: prever
            color: "#ffffff"
            text:  btnMenuEsquerdo.text
            font: btnMenuEsquerdo.font
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: parent.left
            anchors.leftMargin: 75
        }
    }





}




/*##^##
Designer {
    D{i:0;autoSize:true;formeditorZoom:2;height:60;width:250}
}
##^##*/
