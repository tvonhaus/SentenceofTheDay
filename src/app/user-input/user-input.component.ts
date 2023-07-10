import { Component } from '@angular/core';

@Component({
  selector: 'app-user-input',
  templateUrl: './user-input.component.html',
  styleUrls: ['./user-input.component.css']
})
export class UserInputComponent {
  userInput: string = ''; // Property to bind to the input box using ngModel

  submitInput() {
    // Access the user's input from the userInput property and handle it
    console.log('Submitted input:', this.userInput);
  }
}
