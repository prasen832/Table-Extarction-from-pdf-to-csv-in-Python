# Table Extraction from PDF to CSV in Python

![pdf](pdf_to_csv.png)

## Obective

The objective of this project is to extract the table on page no.54 in the given PDF and convert it into a CSV file.

### Why are tables Extraction from pdf's are challenging ?

**Extracting tables from PDFs can be challenging for several reasons**

#### 1. PDF Format Variation:

PDF documents can be created in various ways, leading to differences in structure and formatting. Some PDFs may store tables as images, while others use text-based structures.

#### 2. Text and Image Mix:

Tables in PDFs may be a mix of text and images, making it challenging to extract structured data. Optical Character Recognition (OCR) might be required for image-based tables.

#### 3. Lack of Standardization:

Unlike HTML, which has a standardized way of representing tables, PDFs lack a consistent standard for table structures. Different software and methods of PDF creation can result in varying layouts.

#### 4. Complex Layouts:

PDFs often contain complex layouts with merged cells, nested tables, and other elements that can complicate the extraction process. Tools need to handle these complexities accurately.
No Semantic Information:

Unlike HTML, which includes semantic information about the structure of the document, PDFs might not provide the same level of semantic information. Identifying headers, rows, and columns can be more challenging.

#### 5. Inconsistent Text Positioning:

Text in PDFs may not always be in a predictable position. The lack of a strict grid structure can make it difficult to determine which text elements belong to specific rows or columns.

#### 6. Security Measures:

Some PDFs may be secured or encrypted, limiting the ability to extract data programmatically. Password protection or other security measures can hinder extraction processes.

#### 7. Character Encoding Issues:

PDFs might use different character encodings, and dealing with character encoding issues during extraction is a common challenge.

To overcome these challenges, developers often use specialized libraries and tools designed for PDF parsing and table extraction. These tools may leverage techniques like OCR for image-based content, heuristics for identifying table structures, and algorithms for handling complex layouts. Despite these challenges, with the right tools and techniques, it is possible to extract tables from PDFs accurately.
