import { Injectable } from '@angular/core';
import socket from 'socket.io-client';


@Injectable({
  providedIn: 'root'
})
export class SolverService {



  serviceMsgList = "";

  constructor() {

    // this.getSocketConnection();
    // this.registerEvents()
    this.getSocketConnectionForAWS()
  }


  /* ---------------------------------------------------------------------------------------------------
  --------------------------- LOCAL --------------------------------------------------------------------
  -----------------------------------------------------------------------------------------------------*/
  socket:any;
  local_socket = 'http://0.0.0.0:9016';
  roomId = 10;


  getSocketConnection() {
    this.socket = socket(this.local_socket + '/xtest');
  }

  registerEvents() {

    this.socket.on('connect', (data: string) => {
      this.socket.emit('join_room', { 'room_id': 10});
    });


    this.socket.on('room_id', (data:any) => {
      console.log('event room_id returned by restapi ' + data['id']);
    });

    this.socket.on('process1', (data:any) => {
      this.serviceMsgList += data['test_msg'] + '\n'
    });
  }


/*----------------------------------------------------------------------------------------------------------
----------------------------------- A W S-------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------*/

webSocket:any;
getSocketConnectionForAWS(){
  /*
    | CLIENT |---------------Handshake message --------------------------->>> |API GATEWAY|
    | CLIENT |<<<--------------acknowledgement + (connection id ) ------------|API GATEWAY|
    | CLIENT | ---------------- PROCESS(solver) request  with connection_id --| SERVER |
    | SERVER | <--> emit messages to API_GATEWAY <---> monitored and read by -| CLIENT |

    SUDO CODE :
         1. send message from ui to aws-api  as handshake (FUN: onopen )
         2. the server(aws-api) will return some random id(connection id) back to  ui as acknowledgement (FUN: onmessage)
         3. Now the connection id will sent back to the server which will continuously emit messages to connection_id
         4. The message emitted can be read on onmessage function
  */

 console.log("Inside Socket conncet AWS")

 // create socket object
 this.webSocket = new WebSocket("wss://aw9shewli6.execute-api.us-east-1.amazonaws.com/production");
 

 // send hanshake message (can be any message or empty string )
 this.webSocket.onopen = function(event){
   this.send(JSON.stringify({"action": "sendmessage", "message": "test1"}));
 }


 // Read messages from server / api-gateway
 // Every returnes message will provide connection_id and  messagez
 this.webSocket.onmessage = function(event){
  //  localStorage.setItem('room_id', JSON.parse(event.data)['connectionId'])
   console.log(`[message] Data received from server: ${event.data}`);
  //  var ms = JSON.parse(JSON.parse(event.data)["msg"])["msg"] + '\\n';
  //  eval("document.getElementsByClassName('solve-response-textarea')[0].value += '"+ms+"'")
 }

 

 
}











}