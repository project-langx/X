---
name: Syntactic Change
about: Describe the new syntactic change or addition you want to see in X
title: "[SYNTAX]"
labels: ''
assignees: ''

---

**Describe the change**

In one or two lines describe the new addition or change in syntax of X that you wish to see.

This requires adding support to the following:

- [ ] Tokenizer
- [ ] Parser
- [ ] Tree Walker
- [ ] Compiler
- [ ] Virtual Machine
- [ ] C Decompiler
- [ ] C++ Decompiler
- [ ] Java Decompiler
- [ ] Python Decompiler

It is not necessary that every change requires changes in all the components, you can uncheck the components as required. Don't worry if you are not sure, just keep all the above components.

A **single PR** should be submitted for all the parts. The commits need **to be separate** for all of them.

**New Grammar**

Copy the entire existing grammar from master and add the required changes to it here, make to surround it with ```. It is completely fine, if you are not able to contribute to this part, just delete this section and we'll figure something out.

**Note**: Changes can be made to the grammar as appropriate. Post the changes to the grammar as a reply in this thread.

**Note**: You can only submit a patch if it is approved by one of the maintainers, otherwise the PR will be rejected.
