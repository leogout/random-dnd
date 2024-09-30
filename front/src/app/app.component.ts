import { Component } from '@angular/core';
import {
  FormBuilder,
  FormGroup,
  FormsModule,
  ReactiveFormsModule,
} from '@angular/forms';
import { MatButton } from '@angular/material/button';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatSelectModule } from '@angular/material/select';
import { RouterOutlet } from '@angular/router';
import { CharacterComponent } from './components/character/character.component';
import { ToolbarComponent } from './components/toolbar/toolbar.component';
import { Character } from './models';
import { ApiService } from './services/api.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    RouterOutlet,
    CharacterComponent,
    ToolbarComponent,
    MatButton,
    MatFormFieldModule,
    MatSelectModule,
    ReactiveFormsModule,
    FormsModule,
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
})
export class AppComponent {
  character: Character | undefined;
  races = [
    { value: 'human', viewValue: 'Human' },
    { value: 'dwarf', viewValue: 'Dwarf' },
    { value: 'elf', viewValue: 'Elf' },
    { value: 'halfling', viewValue: 'Halfling' },
    { value: 'half-orc', viewValue: 'Half Orc' },
  ];

  languages = [
    { value: 'french', viewValue: 'French' },
    { value: 'english', viewValue: 'English' },
  ];

  form!: FormGroup;

  constructor(private api: ApiService, private fb: FormBuilder) {}

  ngOnInit() {
    this.form = this.fb.group({
      race: 'human',
      language: 'french',
    });
  }

  generateCharacter() {
    const race = this.form.get('race')?.value;
    const language = this.form.get('language')?.value;
    this.api.generateCharacter(race, language).subscribe((character) => {
      this.character = character;
    });
  }
}
