export default class Day02 {
    constructor() {
        this.day = 'dia02';
        this.table_of_contents_title = 'capítulo 1 Introdução';
        this.topics = [
            'capítulo 1 Introdução'
        ];
    }

    show() {
        for (const i of this.topics) {
            console.log(i);
        }
    }
}
