class Day01 {
    constructor() {
        this.day = 'dia01';
        this.table_of_contents_title = 'Table of Contents';
        this.topics = [
            'About the Author',
            'About_the_Technical_Reviewer',
            'Acknowledgments',
            'Introduction',
        ];
    }

    show() {
        for (const i of this.topics) {
            console.log(i);
        }
    }
}

let day01 = new Day01();
day01.show();
