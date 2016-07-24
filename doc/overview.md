# An (experimental) catalogue of medieval Aristotelian commentaries

This Django application is conceived as a database for registering and analyzing
sources for the medieval Aristotelian tradition. The application is simple. It
is basically a register designed to handle the many to many relations of texts,
authors, manuscripts and locations that make up the landscape of scholastic
texts.

It currently mainly contains material on the tradition on *De anima* as that is
the object of my PhD project, but as there is no difference between commentaries
on *De anima* and any other Aristotelian works, it should handle those just as
well.

A note of caution (vanity?):
The application is for now just a tool for handling and storing my own material.
Some elements of the model are not properly thought out and therefore not in
great use, but the main modules (`manuscripts` and `commentaries`) satisfy my
current need. There are several layers of cruft and some corners of the data
structure that should probably be revised if I had the time and need. But that
is not now.


## Overview of the application

Currently mostly contains material on *De anima*. On the other hand, I think it
might be at least one of the most complete list of commentaries on *De anima* in
existence, as it includes all the material in Weijer, Lohr, and Mora-Márquez's
publications, as well as material that is not contained in any of those nor
other conventional lists.

Some numbers. The database currently (July 2016) contains:
- 302 ancient and medieval texts are registered with information on
  their author, type, date, century, authenticity, among much more.
- 219 manuscripts, with information on location, dating, content, and a range of
  codicological data.
- 104 different authors (the renowned Anonymus being responsible for 122 of the
  302 texts!).
- 352 content registrations, that is, an manifestation of a work in a manuscript.


## Main modules

Let me briefly present the most important modules, which are `Manuscript`,
`Text` and `Places`. This description can be used in combination with the
graphical illustration of the structure in
(partial-schema.png)[partial-schema.png].


### Manuscripts

The manuscripts module is the largest and most complex of the modules. Its main
model is the `Manuscript` model which contains much of the basic information of
a given manuscript. 


`Manuscript` contains the following regular fields:
- `shelfmark`: The shelfmark of the manuscript.
- `number`: The number of the manuscript.
- `olim`: Previous shelfmark and number.
- `saeculo`: Indcates which century the manuscript has been dated to.
- `date`, `date_earliest`, `date_latest`: Together these indicate the dating of
  the manuscript.
- `height` and `width`: Indicates the dimensions of the manuscript. Originally
  `dimension_note` was devised to make a note specific to this, in particular
  whether it is my own measurement or taken from a catalogue and note when it is
  measure in inches rather than millimeters.
- `folios`: Count of folios and front- and back-leafs, usually written like so:
  "267+vi".
- `layout`: Field containing a prose description of the layout of the
  manuscript.
- `script`: Notes on the script(s) and hands of the manuscript.
- `annotation`: Notes on the annotations of the manuscript (type, locations,
  extent).
- `note`: General notes on the manuscript. This most often pertains to
  considerations of dating or content.
- `literature`: References to literature on the manuscript.

`Manuscript` has foreign key id fields to:
- `ManuscriptOrigin`: The model indicating the origin of the manuscript. Aside from the
  timestamp fields and id, this model only contains a reference to the country
  and town of origin as well as a boolean field indicating whether the origin
  reference is dubious or not. This model is hardly used.
- `country`, `town` and `library` which are connected. See the notes on the
  `Places` module below
  
`Manuscript` can be referred to from the following models which contain
foreign key fields to the `Manuscripts` model:
- `ManuscriptContentCommentary`: The most important of the models pointing to
  `Manuscript`. This model contains information about the content of the
  manuscript. It has two foreign key pointers, one to the `Manuscript` model and
  one to the `Text` model. This model contains some basic information about the
  location of the expression of the work in the manuscript as well as fields for
  *incipit* and *explicit* and a note. The name is not optimum,
  `ManuscriptContent` would be much better, but renaming things in Django scares
  me (this has given particular problems in the `Text` model). 
- `OnlineMaterial`: Model containing a URL Field with material relevant to the
  manuscript it points to.
- `ReproductionWishlist`: Each entry refers to a manuscript (or part of it) that
  I would like a reproduction of.
- `Reproduction`: Contains data about the reproduction (that I have some sort of
  access to) of the referred manuscript.
- `ManuscriptInspection`: Contains information about inspections of the
  manuscript referred to, either by me or somebody else (relevant to my work),
  either in digital or physical form.

The `Manuscripts` model raises a unique problem connected with the physical
nature of the medieval codex. Often a codex contains contains material that has
originally belonged to two or more separate manuscripts. This distinction
between codex and manuscript is conflated in the current model. This makes
representing *Sammelhandschriften* impossible. Now I just make notes on it in
the `note`-field, but that is a sub-optimal solution to say the least.


### Commentaries/Text

This model represents a given work, abstract from its specific expressions. It
includes text which might be considered authority texts (such as Aristotle's *De
anima*) as well as commentaries (Aquinas's *Sententia in De anima Aristotelis*).
The problem is that this distinction between commentaries and authority texts is
fluid as you also find commentaries on commentaries. A standard example would be
commentaries on Porphyry's *Isogage*, which itself might be considered a sort of
commentary (or introduction) to Aristotle's *Categories*. When all texts are
collected in one model I this is solved by simple self-reference, but with the
disadvantage of the model be less specific (and hence more empty fields in some
entries). 

The foreign key fields of the model are:
- `author`: The author of the text. Right now it points to fields in the model
  `Commentator`, which also contains authors like Aristotle, who is clearly not
  a commentator. This sucks, but is a vestige of a renaming history similar to
  the one sketched in the section *Problems* below.
- `commentary_on`: Self-reference. Commentaries are commentaries on texts, so
  this reference should be to an instance of the Text model.
- `commentary_type`: Reference to an entry in a table of commentary types.
- `related_commentaries`: Self-reference used for any kind of relation to
  another commentary. Rarely used.

The regular fields of the model are:
- `title` and `title_addon`: Together they indicate the title of the work. The
  `title_addon` field is used for well known alternative names like *Anonymus
  Gautier* or notes on recension or version.
- `text_type`: Currently the possible values of this field are `Authority text`,
  `Commentary`, `Summa or tractatus`, and `Compilation or excerpts`. At the
  application level there is the restriction that a text can only point to
  another text in the `commentary_on`-field that has the type `Authority text`
  in this field. This is a measure to keep down the possible choices in the drop
  down of the `commentary_on` field at a tolerable level. This is also a not
  quite optimum solution.
- `authorship`: Used to indicate whether the authorship of the text is certain
  or not.
- `saeculo`, `date`, `before`, `after`: The dating fields.
- `incipit` and `explicit`: The incipit and explicit of the abstract work. Since
  that is often the text as it is established in a critical edition, they might
  not always have any content, or their content might not be identical to the
  incipit and explicit of an entry in the `ManuscriptContentCommentary` model.
- `note` and `literature`: For notes and listing of literature references.
- `edition_coverage`: Indicates whether the text is covered by a published text.
  Currently the values are `None`, `Full`, `Partial`, `Early print`.
- `mora_reference`: The number in Ana Maria Mora-Márquez's “A List of
  Commentaries on Aristotle’s De anima III (c. 1200 – c. 1400)”, *Cahiers de
  l'Institut du Moyen-Âge grec et latin* 83, 2014, Copenhagen: 207--256.
- `relevance`: Indicating the relevance of the text to my PhD project.

The following models have foreign key references to `Text`:
- `author_alternative`: In case there multiple possible authors, this model
  cross refers the Commentator (should be Author) and the Text models with a
  note field.
- `Attachment`: Used for uploading media relevant to the text to the
  application.
- `ManuscriptContentCommentary`: The important cross model used to connect the
  work with expressions of it and their manifestations in manuscripts. See more
  on this model above under *Manuscript*.



#### Problems

I have a naming problem with this module. It was originally called `Commentary`,
which in combination with `Translation` and `AuthorityText` made up the types of
texts for the application. They were all subclasses of a general text class (the
name of which eludes me at the moment). This gave some problems of inheritance,
mostly that it was not straight forward to let a commentary be on an
Authority-text as well as a Commentary or Translation-text. So I collected the
three types in the general `Text` model.

There is a problem parallel to this in the `Persons` module between the models
`Commentator`, `Authority` and `Translator`, which are all abstract subclasses
of `Author`. But it really sucks and should be changed.

### Places

The places module provides models for geographical locations and libraries used
in other modules. It is mostly (it not only) used in the `Manuscript` module.


The models are:
- `Country`: Provides all the countries of the ISO 3166-1 list as possible
  choices. The model used the Django module
  (django-countries)[https://github.com/SmileyChris/django-countries] to provide
  the list.
- `Town`: Each town much belong to a country.
- `Library`: A library belongs to a country and town.

The relation between the models of this module is special. On the application
level they are chained together in such a way that the selection of country and
town values determine which libraries are available for selection. This means
that when select France from a dropdown when filling out a Manuscript form, then
content of the `Town` field is restricted to those that are in France. When I
select a town (say Paris) the libraries that are located in Paris are available
in the library dropdown.


## Database architecture

Currently the application is configured to run on a *Postgresql* database hosted
on a AWS instance. 

All database models are subclasses of the `BaseModel` which simply adds
timestamp fields on all the tables.


## General challenges and problems

### Performance

Currently, this is the main problem of the application. Due to the directedness
of foreign key relations reverse lookups are unpleasantly slow. Say for instance
that I want to know which manuscripts contain expressions of a given text. This
results in a database query that goes through all entries in the
`ManuscriptContentCommentary` table to see if the value of the field `content`
is identical to the id of my text, and if so, get the information about the
manuscript from the related `manuscript` id. Currently, the admin view of the
`Text` module presents a list where there is made such a look up for each text.
Currently, with just 302 entries in the Text table and 219 in the Manuscript
table, it takes a couple of seconds. It is most pessimum.

### The dating system

Currently the dating of manuscripts and texts is indicated by the use of three
fields, `date`, `date_earliest`, and `date_latest`. The `date`-field contains
a specific date, as exact as possible, of the item. The two remaining fields are
used to indicate a *terminus post* and *ante quem* of the item. 

The `date`-field poses a challenge as it might contain exact dates (in ISO
format), usually a specific year such as 1291, or maybe a more exact date such
as 1276-05-23. 

The `saeculo` field contains a dating according to century. If the content is a
century, it is (usually) indicated by a prefixed "s. ", so "s. 13" would
indicate "13th century", "s. 13-14" would indicate "13th or 14th century". When
referring to centuries I occasionally segment them in quarters separated by a
full stop. So "s. 13.4" and "s. 13.3-14.1" means "4th quarter of 13th century"
and "third quarter of 13th century to first quarter of 14th century".

Cirka dates are usually indicated with a prefixed "ca. ".

Doubtful dates are usually indicated with a suffixed "?"

This is obviously a mess. It would be great to devise a simple and unambiguous
way of indicated centuries and exact dates which incorporating uncertain and
approximate dates.

