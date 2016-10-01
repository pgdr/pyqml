import QtQuick 1.0

Rectangle {
    signal clicked
    signal shutdownRequested
    focus: true
    Keys.onPressed: {
        if (event.key == Qt.Key_Q) {
            console.log("shutdown requested")
            shutdownRequested()
        }
    }

    function updateMessage(text) {
        messageText.text = text
    }
    
    anchors.fill: parent
    color: "#fff"
    
    Text {
        id: messageText
        anchors.left: parent.left
        font.pointSize: 14
        color: "#c0b"
    }

    Text {
        id: rightMessage
        anchors.left: messageText.right
        anchors.leftMargin: 4
        font.pointSize: 14
        color: "#c9f900"
        text: " rightmost.  Click Q to QUIT"
    }

    
    MouseArea {
        anchors.fill: parent
        onClicked: parent.clicked()
    }
}
