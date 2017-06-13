
### Indexing / Selection
The basics of indexing are as follows:

|Operation|Syntax|Result|
|:-:|:-:|:-:|
|Select column	                |df[col]        |Series|
|Select row by label	        |df.loc[label]  |Series|
|Select row by integer location |df.iloc[loc]   |Series|
|Slice rows	                    |df[5:10]       |DataFrame|
|Select rows by boolean vector  |df[bool_vec]   |DataFrame|