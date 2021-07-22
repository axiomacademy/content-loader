# content-loader
Loads the knowledge graph data into dgraph, using a declarative YAML syntax

# Content labelling system
For ease of indexing, it makes sense to have a content indexing system which enables easy referral to a particular piece of content, and to identify it's type. Rather than just rely on unique UIDs.

Refer to the [Dewey Decimal System](https://en.wikipedia.org/wiki/Dewey_Decimal_Classification) for more info.

We have 5 major content topics- Science, Technology, Arts, Humanities, Mathematics.
Each of these, correspond to a unique leading sequence as follows.

| Science | Technology | Arts | Humanities | Mathematics |
| --- | --- | --- | --- | --- |
| S | T | A | H | M |

This is joined to an unique 4 digit number from 0000 to 9999, representing up to 10000 topics. An example would be a topic, Introduction to Drawing with a code **A-0001**.

Then, this is followed by another 3 digit code for the content type. That can be read from the legend below
| Range | Content Type |
| --- | --- |
| 000 - 099 | Lecture (100 max) |
| 100 - 199 | Challenge (100 max) |
| 200 - 299 | Tutorial (100 max) |

So an example would be, **A-0001-145** which can be read as an Arts topic, with id 001, and it's a challenge with id 45.
