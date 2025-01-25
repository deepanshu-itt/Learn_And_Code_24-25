// Does this Book class follow SRP?  

class Book {
 
    function getTitle() {
        return "A Great Book";
    }
 
    function getAuthor() {
        return "John Doe";
    }
}

class Library extends Book{
    function getLocation() {
        // returns the position in the library
        // ie. shelf number & room number
    }

    function save() {
        $filename = '/documents/'. $this->getTitle(). ' - ' . $this->getAuthor();
        file_put_contents($filename, serialize($this));
    }
}

class BookReader extends Book{
    function turnPage() {
        // pointer to next page
    }
 
    function getCurrentPage() {
        return "current page content";
    }
}

interface Printer {
 
    function printPage($page);
}
 
class PlainTextPrinter implements Printer {
 
    function printPage($page) {
        echo $page;
    }
 
}
 
class HtmlPrinter implements Printer {
 
    function printPage($page) {
        echo '<div style="single-page">' . $page . '</div>';
    }
}

<!-- From my Opinion the Class is not following the SRP as the Book Class has more than single responsibility
the class should manage the operations related to managing books like getTitle, getAuthor,turnPage,getCurrentPage 
but for saving the book and for getLocation does not fit in this class we should have different class 
for this like Library class where we can manage operations related to library.
In Conclusion the Book Class doesn't follow SRP.  -->