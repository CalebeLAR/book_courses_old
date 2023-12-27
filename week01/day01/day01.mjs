export default class Day01 {
    constructor() {
        this.day = 'dia01';
        this.table_of_contents_title = 'Agradecimentos';
        this.topics = [
            'Agradecimentos',
            'Sobre_o_autor',
            'Prefácio'];
    }

    show() {
        for (const i of this.topics) {
            console.log(i);
        }
    }
}

