var topic = "xquest/test";
var client_id = "xquest_"+Math.floor((1 + Math.random()) * 0x10000000000).toString(12);
// Create a client instance: Broker, Port, Websocket Path, Client ID
const client = new Paho.MQTT.Client("broker.hivemq.com", Number(8000), "/mqtt", "tqtqt");

client.connect({
	
});
// set callback handlers
client.onConnectionLost = function (responseObject) {
    console.log("Connection Lost: "+responseObject.errorMessage);
}

client.onMessageArrived = function (message) {
  console.log("Message Arrived: "+message.payloadString);
}

function mySendMessage(x) {
  var message = new Paho.MQTT.Message(x);
      message.destinationName = topic;
      message.qos = 0;
      client.send(message);
      console.log("message sent");
}
function uplift() {
    mySendMessage("Up")
  }
  function downlift() {
    mySendMessage("Down")
  }
  function leftlift() {
    var checkBox = document.getElementById("blueCheck");
    mySendMessage("Left")
  }
  function rightlift() {
    mySendMessage("Right")
    
  }
  function forwardlift() {
    mySendMessage("Forward")
    
  }
  function backwardlift() {
    mySendMessage("Backward")
    
  }
  function reset1() {
    mySendMessage("reset1")
    //up and down
  }
  function reset2() {
    mySendMessage("reset2")
    //straight
  }
  function camera()
 {
    var x = document.getElementById("bsx");
    if (x.innerHTML === "CAMERA!") {
        x.innerHTML = "STREAMING!";
      } else {
        x.innerHTML = "CAMERA!";
      }
    mySendMessage("Camera")
 }