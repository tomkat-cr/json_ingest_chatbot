# CHANGELOG

All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/) and [Keep a Changelog](http://keepachangelog.com/).



## Unreleased
---

### New

### Changes

### Fixes

### Breaks


## 0.1.1 (2023-07-20)
---

### New
Add Git repository reading.
Add visual design as ChatGPT, with the input text at the bottom.

### Fixes
JSON ingest assigns page_content with the whole json content.
Fix broken icon images. The only way to do it to use a public URL in the `src` attribute. Locals does not work.
JSON file `page_content` is not the file title, is the file content as serialized string. This expands the context.


## 0.1.0 (2023-06-29)
---

### New
First JSON ingest version with fixing assignment of page_content based on the JSON filename.
