import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { TitleComponent } from './title/title.component';
import { WordOfTheDayComponent } from './word-of-the-day/word-of-the-day.component';
import { UserInputComponent } from './user-input/user-input.component';


@NgModule({
  declarations: [
    AppComponent,
    TitleComponent,
    WordOfTheDayComponent,
    UserInputComponent
  ],
  imports: [
    BrowserModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
