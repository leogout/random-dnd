import {ComponentFixture, TestBed} from '@angular/core/testing';

import {CharacterComponent} from './character.component';
import {Character, Loot} from "../../models";

describe('CharacterComponent', () => {
  let component: CharacterComponent;
  let fixture: ComponentFixture<CharacterComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CharacterComponent]
    })
      .compileComponents();

    fixture = TestBed.createComponent(CharacterComponent);
    component = fixture.componentInstance;
    fixture.componentRef.setInput('character', {
      race: "",
      full_name: "",
      gender: "",
      description: "",
      attitude: "",
      loot: [],
      quest: "",
    } as Character);
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
