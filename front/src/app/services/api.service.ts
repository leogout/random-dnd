import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Character } from '../models';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  constructor(private http: HttpClient) {}

  generateCharacter(race: string, language: string): Observable<Character> {
    return this.http.get<Character>('http://127.0.0.1:8000/character', {
      params: {
        race,
        language,
      },
    });
  }
}
