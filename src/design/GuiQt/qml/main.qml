import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import "controles"
import QtGraphicalEffects 1.15

Window {
    id: mainWindow
    width: 1000
    height: 580
    minimumWidth: 800
    minimumHeight: 500

    visible: true
    color: "#00000000"

    flags: Qt.Window | Qt.FramelessWindowHint



    property int statusJanela: 0
    property int margemJanela: 10

    QtObject{
        id:internal

        function resetResizeBorda(){
            resizeBaixo.visible = true
            resizeCima.visible = true
            resizeDireita.visible = true
            resizeEsquerda.visible = true
            resizeDiagBD.visible = true
        }


        function maximizeRestore() {
            if(statusJanela == 0){
                statusJanela = 1
                margemJanela = 0
                mainWindow.showMaximized()
                resizeBaixo.visible = false
                resizeCima.visible = false
                resizeDireita.visible = false
                resizeEsquerda.visible = false
                resizeDiagBD.visible = false
                maximizar.btnIconeSource = "../imagens/svg_imagens/restaurar.png"
            }
            else{
                statusJanela = 0
                margemJanela = 10
                mainWindow.showNormal()
                internal.resetResizeBorda()
                maximizar.btnIconeSource = "../imagens/svg_imagens/maximizar.png"
            }
        }
        function ifMaximizedWindowRestore(){
            if(statusJanela == 1){
                mainWindow.showNormal()
                statusJanela = 0
                margemJanela = 10
                internal.resetResizeBorda()

            }
        }

        function restaurarMargem(){
            margemJanela = 10
            statusJanela = 0
            internal.resetResizeBorda()
        }

    }




    title: qsTr("Basketball Prediction")

    Rectangle {
        id: background
        color: "#1d1d1d"
        border.color: "#24242d"
        border.width: 1
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.leftMargin: margemJanela
        anchors.topMargin: margemJanela
        anchors.bottomMargin: margemJanela
        anchors.rightMargin: margemJanela
        z:1

        Rectangle {
            id: imagemCentral
            x: 70
            y: 60
            width: 1000
            height: 580
            color: "#00000000"
            anchors.fill: parent
            anchors.bottomMargin: 0
            anchors.rightMargin: 0
            anchors.leftMargin: 70
            anchors.topMargin: 60
        }

        Rectangle {
            id: appContainer
            color: "#00000000"
            anchors.fill: parent

            Rectangle {
                id: topBar
                height: 60
                color: "#2e2626"
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.rightMargin: 0
                anchors.leftMargin: 0
                anchors.topMargin: 0

                BotaoExtensor{
                    btnCorDefault: "#2a2323"
                    btnCorMouseHover: "#1e1919"
                    btnCorClique: "#3e3333"
                    onClicked: animacaoMenu.running = true

                }

                Rectangle {
                    id: descricaoTop
                    y: 20
                    height: 25
                    color: "#3c3e40"
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.bottom: parent.bottom
                    anchors.rightMargin: 0
                    anchors.leftMargin: 70
                    anchors.bottomMargin: 0

                    Label {
                        id: descricao
                        color: "#ffffff"
                        text: "descrição 1"
                        anchors.left: parent.left
                        anchors.right: parent.right
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        verticalAlignment: Text.AlignVCenter
                        wrapMode: Text.NoWrap
                        font.family: "Courier"
                        font.weight: Font.Normal
                        textFormat: Text.RichText
                        anchors.rightMargin: 300
                        anchors.leftMargin: 10
                        anchors.bottomMargin: 0
                        anchors.topMargin: 0
                    }

                    Label {
                        id: descricao2
                        color: "#ffffff"
                        text: "| Página Inicial"
                        anchors.left: descricao.right
                        anchors.right: parent.right
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        horizontalAlignment: Text.AlignRight
                        verticalAlignment: Text.AlignVCenter
                        wrapMode: Text.NoWrap
                        font.family: "Courier"
                        anchors.leftMargin: 0
                        anchors.bottomMargin: 0
                        anchors.topMargin: 0
                        textFormat: Text.RichText
                        anchors.rightMargin: 10
                        font.weight: Font.Normal
                    }
                }

                Rectangle {
                    id: titulo
                    height: 35
                    color: "#00000000"
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.top: parent.top
                    anchors.rightMargin: 105
                    anchors.leftMargin: 70
                    anchors.topMargin: 0

                    DragHandler{
                        onActiveChanged: if(active){
                                             mainWindow.startSystemMove()
                                             internal.ifMaximizedWindowRestore()
                                         }
                    }

                    Image {
                        id: iconeapp
                        width: 28
                        anchors.left: parent.left
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        source: "../imagens/svg_imagens/iconeA.png"
                        anchors.bottomMargin: 0
                        anchors.leftMargin: 5
                        anchors.topMargin: 0
                        fillMode: Image.PreserveAspectFit
                    }

                    Label {
                        id: tituloapp
                        color: "#ffffff"
                        text: qsTr("Basketball Prediction Tool")
                        anchors.left: iconeapp.right
                        anchors.right: parent.right
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        horizontalAlignment: Text.AlignLeft
                        verticalAlignment: Text.AlignVCenter
                        font.family: "Courier"
                        font.pointSize: 15
                        anchors.leftMargin: 5
                    }
                }

                Row {
                    id: botoesSistema
                    x: 490
                    width: 105
                    height: 35
                    anchors.right: parent.right
                    anchors.top: parent.top
                    anchors.topMargin: 0
                    anchors.rightMargin: 0

                    BotaoTopBar{
                        id: minimizar
                        onClicked:{

                            mainWindow.showMinimized()
                            internal.restaurarMargem()

                        }
                    }

                    BotaoTopBar {
                        id: maximizar
                        btnIconeSource: "../imagens/svg_imagens/maximizar.png"
                        onClicked: internal.maximizeRestore()
                    }

                    BotaoTopBar {
                        id: fechar
                        btnCorClique: "#ff0000"
                        btnIconeSource: "../imagens/svg_imagens/fechar.png"
                        onClicked: mainWindow.close()
                    }
                }
            }

            Rectangle {
                id: conteudo
                visible: true
                color: "#00000000"
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: topBar.bottom
                anchors.bottom: parent.bottom
                clip: false
                anchors.topMargin: 0

                Rectangle {
                    id: menuEsquerda
                    width: 70
                    color: "#2a2323"
                    anchors.left: parent.left
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom
                    clip: true
                    anchors.leftMargin: 0
                    anchors.bottomMargin: 0
                    anchors.topMargin: 0

                    PropertyAnimation{
                        id: animacaoMenu
                        target: menuEsquerda
                        property: "width"
                        to: if(menuEsquerda.width == 70) return 200; else return 70
                        duration: 1000
                        easing.type: Easing.OutBack
                        //easing.type: Easing.InOutQuint



                    }

                    Column {
                        id: column
                        width: 70
                        anchors.left: parent.left
                        anchors.right: parent.right
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        clip: true
                        anchors.rightMargin: 0
                        anchors.leftMargin: 0
                        anchors.bottomMargin: 90
                        anchors.topMargin: 0

                        BtnMenuEsquerdo {
                            id: btnMenuPrever
                            width: menuEsquerda.width
                            text: "Prever!"
                            btnCorDefault: "#2a2323"
                            activeMenuColor: "#e66508"
                            iconWidth: 30
                            iconHeigth: 60
                            menuEstaAtivo: true
                            onClicked: {
                                btnMenuPrever.menuEstaAtivo = true
                                btnMenuPPassadas.menuEstaAtivo = false
                                btnMenuSobre.menuEstaAtivo = false
                                btnConfig.menuEstaAtivo = false

                                stackView.push(Qt.resolvedUrl("paginas/preverPage.qml"))
                            }

                        }

                        BtnMenuEsquerdo {
                            id: btnMenuPPassadas
                            width: menuEsquerda.width
                            text: "Partidas Passadas"
                            btnIconeSourc: "../imagens/svg_imagens/ppassadas.png"
                            iconHeigth: 60
                            activeMenuColor: "#e66508"
                            menuEstaAtivo: false
                            iconWidth: 30
                            btnCorDefault: "#2a2323"

                            onClicked: {
                                btnMenuPrever.menuEstaAtivo = false
                                btnMenuPPassadas.menuEstaAtivo = true
                                btnMenuSobre.menuEstaAtivo = false
                                btnConfig.menuEstaAtivo = false

                                stackView.push(Qt.resolvedUrl("paginas/ppPage.qml"))
                            }
                        }

                        BtnMenuEsquerdo {
                            id: btnMenuSobre
                            width: menuEsquerda.width
                            text: "Sobre"
                            btnIconeSourc: "../imagens/svg_imagens/sobre.png"
                            iconHeigth: 60
                            activeMenuColor: "#e66508"
                            menuEstaAtivo: false
                            iconWidth: 30
                            btnCorDefault: "#2a2323"

                            onClicked: {
                                btnMenuPrever.menuEstaAtivo = false
                                btnMenuPPassadas.menuEstaAtivo = false
                                btnMenuSobre.menuEstaAtivo = true
                                btnConfig.menuEstaAtivo = false

                                stackView.push(Qt.resolvedUrl("paginas/sobrePage.qml"))
                            }
                        }




                    }

                    BtnMenuEsquerdo {
                        id: btnConfig
                        x: 0
                        y: 415
                        width: menuEsquerda.width
                        text: "Configurações"
                        anchors.bottom: parent.bottom
                        clip: false
                        anchors.bottomMargin: 25
                        iconHeigth: 60
                        btnCorDefault: "#2a2323"
                        menuEstaAtivo: false
                        btnIconeSourc: "../imagens/svg_imagens/settings.png"
                        activeMenuColor: "#e66508"
                        iconWidth: 30
                        onClicked: {
                            btnMenuPrever.menuEstaAtivo = false
                            btnMenuPPassadas.menuEstaAtivo = false
                            btnMenuSobre.menuEstaAtivo = false
                            btnConfig.menuEstaAtivo = true

                            stackView.push(Qt.resolvedUrl("paginas/configPage.qml"))
                        }
                    }
                }


                Rectangle {
                    id: conteudoPagina
                    color: "#00000000"
                    anchors.left: menuEsquerda.right
                    anchors.right: parent.right
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom
                    clip: true
                    anchors.rightMargin: 0
                    anchors.leftMargin: 0
                    anchors.bottomMargin: 25
                    anchors.topMargin: 0

                    StackView {
                        id: stackView
                        anchors.fill: parent
                        initialItem: Qt.resolvedUrl("paginas/preverPage.qml")
                    }



                }


                Rectangle {
                    id: rectangle
                    x: 70
                    y: 0
                    color: "#3c3e40"
                    anchors.left: menuEsquerda.right
                    anchors.right: parent.right
                    anchors.top: conteudoPagina.bottom
                    anchors.bottom: parent.bottom
                    anchors.rightMargin: 0
                    anchors.leftMargin: 0
                    anchors.bottomMargin: 0
                    anchors.topMargin: 0

                    Label {
                        id: notaDeRodape
                        color: "#ffffff"
                        text: "A project by: Bernardo Mesko. Gregori Sabel, Joao V Waldrich & Rafael G. Onesko"
                        anchors.left: parent.left
                        anchors.right: parent.right
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        verticalAlignment: Text.AlignVCenter
                        wrapMode: Text.NoWrap
                        anchors.leftMargin: 10
                        anchors.bottomMargin: 0
                        anchors.topMargin: 0
                        font.family: "Courier"
                        textFormat: Text.RichText
                        anchors.rightMargin: 30
                        font.weight: Font.Normal
                    }
                }

                MouseArea {
                    id: resizeDiagBD
                    x: 925
                    y: 475
                    width: 25
                    height: 25
                    anchors.right: parent.right
                    anchors.bottom: parent.bottom
                    anchors.rightMargin: 0
                    anchors.bottomMargin: 0
                    cursorShape: Qt.SizeFDiagCursor

                    Image {
                        id: image1
                        anchors.left: parent.left
                        anchors.right: parent.right
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        source: "../imagens/svg_imagens/resize.png"
                        anchors.rightMargin: 0
                        anchors.leftMargin: 0
                        anchors.bottomMargin: 0
                        anchors.topMargin: 0
                        fillMode: Image.PreserveAspectFit
                    }

                    DragHandler{
                        target: null
                        onActiveChanged: if (active) { mainWindow.startSystemResize(Qt.RightEdge | Qt.BottomEdge)}
                    }

                }


            }
        }


    }



    DropShadow{
        anchors.fill: background
        horizontalOffset: 0
        verticalOffset: 0
        radius: 10
        samples: 16
        color: "#80000000"
        source: background
        z:0
    }

    MouseArea {
        id: resizeEsquerda
        width: 10
        anchors.left: parent.left
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.topMargin: 10
        anchors.bottomMargin: 10
        anchors.leftMargin: 0
        cursorShape: Qt.SizeHorCursor

        DragHandler{
            target: null
            onActiveChanged: if (active) { mainWindow.startSystemResize(Qt.LeftEdge)}
        }

    }

    MouseArea {
        id: resizeDireita
        width: 10
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.rightMargin: 0
        anchors.topMargin: 10
        anchors.bottomMargin: 10
        cursorShape: Qt.SizeHorCursor

        DragHandler{
            target: null
            onActiveChanged: if (active) { mainWindow.startSystemResize(Qt.RightEdge)}
        }

    }

    MouseArea {
        id: resizeBaixo
        x: 918
        y: 40
        height: 10
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.rightMargin: 10
        anchors.bottomMargin: 0
        anchors.leftMargin: 10
        cursorShape: Qt.SizeVerCursor

        DragHandler{
            target: null
            onActiveChanged: if (active) { mainWindow.startSystemResize(Qt.BottomEdge)}
        }

    }

    MouseArea {
        id: resizeCima
        height: 10
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.rightMargin: 10
        anchors.topMargin: 0
        anchors.leftMargin: 10
        cursorShape: Qt.SizeVerCursor

        DragHandler{
            target: null
            onActiveChanged: if (active) { mainWindow.startSystemResize(Qt.TopEdge)}
        }

    }











}





/*##^##
Designer {
    D{i:0;formeditorZoom:0.66}
}
##^##*/
