# Air Blocks
Decentralised Aircraft Document Logging Service

## Introduction

Aviation is a highly regulated industry. That is what keeps it safe. The entire lifecycle of an aircraft is tightly controlled, from design through manufacture to operations.

In order to maintain this level of airworthiness, there are regular processes done by licenced and authorised personnel. These processes are carried out in accordance with the relevant manufacturer's and regulatory authority's approved procedures and directives.

Storing and documenting logs of these processes accurately is vital as part of the accountable chain of proof for an aircraft's airworthiness, and must be retrievable even in the event of a single backend failure. They are also need to be read by external organisations who wish to trace the exact and true history of an aircraft's legal basis for airworthiness.

This repository contains the basis for building a Hyperledger blockchain network and application for storing aircraft airworthiness logs.

## Pre-requisites

It is expected that a Hyperledger Fabric network has been created and provisioned as per the official documentation, with the following configuration:

- One channel per aircraft in the fleet (e.g. a channel for F-WTSS, another for G-BSST, etc).
- One primary organisation that will submit transactions to the network (with CA certificates issued).
- Users pre-registered on the organisation.

The network can be provisioned on-premise or in a public cloud environment. The major vendors have guidance on how to set up blockchain networks.

The expectation is that clients will access the network via secured machines, virtual or physical. Chaincode invocation will be through a browser client. As part of the setup:

- The client machines have the CA certificates pre-installed.
- The user identities and connection profiles have been added into the Origin Private File System (OPFS) of the browser.

### Recommended stack

This is the recommended stack for this application:

- Hyperledger Fabric v2.2 LTS on a public cloud provider
- Chrome v108 or higher that can securely access the network

## Installation

This repository has been split into a chaincode section and an application section.

1. Complete the network and application requirements in the `Pre-requisites` section of this README.
1. Go to `chaincode/`.
1. Deploy the chaincode to each channel.
1. Go to `application/`.
1. Build the Svelte web app.
1. Deploy the web app to each client machine.

## Operation

Each document is added via the web form. Enter the Aircraft Registration (determines channel), Document type (A-Check, C-Check, etc), the date, and the document contents.

The Document type is the identifier. This means the World State for each channel (i.e. each aircraft) will contain the latest documents of each type, making retrieval convenient. Historical documents of the same type will be part of the blocks, and can be retreived via deep queries.

A SHA256 sum of the document content is also stored in the block.
