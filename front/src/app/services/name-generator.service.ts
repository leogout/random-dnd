import { Injectable } from '@angular/core';
import { Races } from '../models/races';

@Injectable({
  providedIn: 'root',
})
export class NameGeneratorService {
  constructor() {}

  generateName(race: Races) {
    const dwarvesNames = [
      'Gimli',
      'Thorin',
      'Balin',
      'Dwalin',
      'Fili',
      'Kili',
      'Oin',
      'Gloin',
      'Mori',
      'Dori',
      'Nori',
    ];

    switch (race) {
      case Races.DWARF:
        return;
    }
  }
}
