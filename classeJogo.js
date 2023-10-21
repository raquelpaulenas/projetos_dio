// Classe genérica que representa um herói de aventura
class Hero {
    constructor(nome, idade, tipo) {
        this.name = nome;
        this.age = idade;
        this.type = tipo;
    }

    fight() {
        let attack;
        switch (this.type) {
            case "mago":
                attack = "usando magia";
                break;
            case "guerreiro":
                attack = "usando espada";
                break;
            case "monge":
                attack = "usando artes marciais";
                break;
            case "ninja":
                attack = "usando shuriken";
                break;
            case "feiticeira":
                attack = "usando magia ancestral"; 
                break;
            case "necromante":
                attack = "usando magia negra";
                break;
            default:
                attack = "atacou";
        }
        console.log(`o ${this.name}, com seus ${this.age} anos de experiência atacou usando ${attack}`);
    }
}

// Exemplo de uso:
const heroi = new Hero("Dr. Facilier", 500 , "necromante");
heroi.fight();