export interface Loot {
  name: string;
  description: string;
}

export interface Character {
  race: string;
  full_name: string;
  gender: string;
  description: string;
  attitude: string;
  loot: Loot[];
  quest: string;
}
