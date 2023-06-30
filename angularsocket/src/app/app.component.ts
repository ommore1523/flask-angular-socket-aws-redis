import { Component, OnInit, DoCheck, Input } from '@angular/core';
import {SolverService} from '../app/solver.service'
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'angularsocket';
  
  messageList:any = "";

  
  constructor(private solveService: SolverService){

  }

  ngOnInit() {

    this.messageList = this.solveService.serviceMsgList;
  }


  ngDoCheck() {
    this.messageList = this.solveService.serviceMsgList;
  }
}


