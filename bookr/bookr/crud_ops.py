def crud_ops():
    from reviews.models import Publisher, Contributor
    publisher = Publisher(name='Packt Publishing', website='https://www.packtpub.com', email='info@packtpub.com')
    publisher.save()
    publisher.email = 'customersupport@packtpub.com'
    publisher.save()
    print(publisher.email)
    contributor = Contributor.objects.create(first_names="Rowel", last_names="Atienza",
                                             email="RowelAtienza@example.com")
    print(contributor)
    print('\n>>> END <<<')


def many_to_one_example():
    from reviews.models import Book, Publisher
    from datetime import date
    publisher = Publisher.objects.get(name='Packt Publishing')
    book = Book.objects.create(title="Advanced Deep Learning with Keras", publication_date=date(2018, 10, 31),
                               isbn="9781788629416", publisher=publisher)
    print(book)
    print('\n>>> END <<<')


def many_to_many_example():
    from reviews.models import Book, Contributor, Publisher
    from datetime import date

    contributor = Contributor.objects.get(first_names='Rowel')

    book = Book.objects.get(title="Advanced Deep Learning with Keras")
    from reviews.models import BookContributor
    book_contributor = BookContributor(book=book, contributor=contributor, role='AUTHOR')
    book_contributor.save()

    book = Book.objects.get(title="Advanced Deep Learning with Keras")

    contributor = Contributor.objects.create(first_names='Packt', last_names='Example Editor',
                                             email='PacktEditor@example.com')

    book.contributors.add(contributor, through_defaults={'role': 'EDITOR'})

    book.contributors.create(first_names='Packtp', last_names='Editor Example', email='PacktEditor2@example.com',
                             through_defaults={'role': 'EDITOR'})

    publisher = Publisher.objects.create(name='Pocket Books', website='https://pocketbookssampleurl.com',
                                         email='pocketbook@example.com')
    contributor1 = Contributor.objects.create(first_names='Stephen', last_names='Stephen',
                                              email='StephenKing@example.com')
    contributor2 = Contributor.objects.create(first_names='Peter', last_names='Straub',
                                              email='PeterStraub@example.com')
    book = Book.objects.create(title='The Talisman', publication_date=date(2012, 9, 25), isbn='9781451697216',
                               publisher=publisher)

    book.contributors.set([contributor1, contributor2], through_defaults={'role': 'CO_AUTHOR'})

    print('\n>>> END <<<')


def get_examples():
    from reviews.models import Publisher

    publisher = Publisher.objects.get(name='Pocket Books')

    print(publisher)
    print(publisher.name)
    print(publisher.website)
    print(publisher.email)
    print(vars(publisher))

    publisher = Publisher.objects.get(website='https://pocketbookssampleurl.com')

    print(publisher.name)
    print(Publisher.objects.get(pk=2))
    print(Publisher.objects.get(id=2))

    from reviews.models import Contributor

    contributors = Contributor.objects.all()

    print(contributors[0])
    print(contributors[0].first_names)
    print(contributors[0].last_names)

    print('\n>>> END <<<')


def filter_example():
    from reviews.models import Contributor, Book
    from datetime import date

    Contributor.objects.create(first_names='Peter', last_names='Wharton', email='PeterWharton@example.com')

    Contributor.objects.create(first_names='Peter', last_names='Tyrrell', email='PeterTyrrell@example.com')

    print(Contributor.objects.filter(first_names='Peter'))
    print(Contributor.objects.filter(first_names='Rowel'))
    print(Contributor.objects.filter(first_names='Nobody'))

    book = Book.objects.filter(publication_date__gt=date(2014, 1, 1))

    print(book)
    print(book[0].publication_date)

    book = Book.objects.filter(title__contains='Deep learning')

    print(book)
    print(book[0].title)
    print(Contributor.objects.all())
    print(Contributor.objects.exclude(first_names='Peter'))

    books = Book.objects.order_by("publication_date")
    print(books)

    print('\n>>> END <<<')


def order_by_example():
    from reviews.models import Book, Publisher, Review, BookContributor, Contributor
    books = Book.objects.order_by("publication_date")
    print(books)
    print(books[0].publication_date)
    print(books[1].publication_date)
    books = Book.objects.order_by("-publication_date")  # opposite order
    print(books)
    print(books[0].publication_date)
    print(books[1].publication_date)
    books = Book.objects.order_by('id')
    print(books[0].id)
    print(books[1].id)
    books = Book.objects.order_by('-id')
    print(books[0].id)
    print(books[1].id)
    books = Book.objects.order_by('title')
    print(books[0])
    print(books[1])
    books = Book.objects.order_by('-title')
    print(books[0])
    print(books[1])

    publishers = Publisher.objects.all().values()
    print(publishers)
    print('\n>>> END <<<')


def query_many_to_many():
    from reviews.models import Contributor, Book
    print(Contributor.objects.filter(book__title='The Talisman'))

    book = Book.objects.get(title='The Talisman')
    print(book.contributors.all())

    contributor = Contributor.objects.get(first_names='Rowel')
    print(contributor.book_set.all())  # Return all the books written by the contributor.
    print('\n>>> END <<<')


def update_example():
    from reviews.models import Contributor, Book
    print(Contributor.objects.filter(last_names='Tyrrell').update(first_names='Mike'))
    print(Contributor.objects.get(last_names='Tyrrell').first_names)
    print('\n>>> END <<<')


def delete_example():
    from reviews.models import Contributor, Book
    print(Contributor.objects.get(last_names='Wharton').delete())
    try:
        print(Contributor.objects.get(last_names='Wharton'))
    except Exception as ex:
        print(type(ex))
        print(ex)
    print('\n>>> END <<<')
