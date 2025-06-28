import { Component, input } from '@angular/core';
import {
  MatCardContent,
  MatCardModule,
  MatCardSubtitle,
  MatCardTitle,
} from '@angular/material/card';
import { Character } from '../../models';

@Component({
    selector: 'app-character',
    imports: [MatCardModule, MatCardTitle, MatCardSubtitle, MatCardContent],
    templateUrl: './character.component.html',
    styleUrl: './character.component.scss'
})
export class CharacterComponent {
  character = input.required<Character>();
}
