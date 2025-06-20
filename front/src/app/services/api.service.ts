import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Character } from '../models';
import {environment} from "../../environments/environment";

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  constructor(private http: HttpClient) {}

  generateCharacter(race: string, language: string): Observable<Character> {
    return this.http.get<Character>(`${environment.apiUrl}/character`, {
      params: {
        race,
        language,
      },
    });
  }
}
