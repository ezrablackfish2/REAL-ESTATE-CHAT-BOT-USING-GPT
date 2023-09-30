function_description = [
        {
            "name": "getTitle",
            "description": "Get the name or title of our hotel what it is recognized by",
            "parameters": {
                "type": "object",
                "properties": {
                    },
                "required": [],
                }
            },
{
            "name": "getHistory",
            "description": "this tells you the history of our hotel getva about the past foundation and who found it the old names also",
            "parameters": {
                "type": "object",
                "properties": {
                    },
                "required": [],
                }
            },
{
            "name": "getDescription",
            "description": "any kind of description about the hotel especially it is general information about it the service and others if the user is new the first thing that should be said is this ",
            "parameters": {
                "type": "object",
                "properties": {
                    },
                "required": [],
                }
            },
{
            "name": "getLocation",
            "description": "if the user want the location of our hotel this is needed",
            "parameters": {
                "type": "object",
                "properties": {
                    },
                "required": [],
                }
            },
{
            "name": "getRules",
            "description": "this tells about the rules and regulations of the hotel what the user must follow",
            "parameters": {
                "type": "object",
                "properties": {
                    },
                "required": [],
                }
            },
{
            "name": "getServices",
            "description": "this tells about all kind of services the hotel provides",
            "parameters": {
                "type": "object",
                "properties": {
                    },
                "required": [],
                }
            },
{
            "name": "getBed",
            "description": "if the user want informtion about the bed service this is detailed information",
            "parameters": {
                "type": "object",
                "properties": {
                    },
                "required": [],
                }
            },
{
            "name": "getFood",
            "description": "if the user wants about the food service we provide in our hotel",
            "parameters": {
                "type": "object",
                "properties": {
                    },
                "required": [],
                }
            },
{
            "name": "getEntertainment",
            "description": "if the user wants information about all kinds of entertainments we provide",
            "parameters": {
                "type": "object",
                "properties": {
                    },
                "required": [],
                }
            },
{
            "name": "getPrice",
            "description": "it provides the price we charge for all kinds of services",
            "parameters": {
                "type": "object",
                "properties": {
                    "service": {
                        "type" : "string",
                        "description": "the type of service we charge the user",
                        "enum": ["food", "bed", "gym", "shower"]
                        }
                    },
                "required": ["service"],
                }
            },


{
            "name": "getAmneties",
            "description": "it provides all types of amenities found in all kinds of room",
            "parameters": {
                "type": "object",
                "properties": {
                    "room": {
                        "type" : "string",
                        "description": "the type of room we have in our hotel",
                        "enum": ["livingroom", "bedroom", "kitchen", "balcony"]
                        }
                    },
                "required": ["room"],
                }
            },
{
            "name": "getContact",
            "description": "this tells about the information needed to contact our staffs or members host where the user can found even our website social medias etc...",
            "parameters": {
                "type": "object",
                "properties": {
                    },
                "required": [],
                }
            },
{
            "name": "getAvailability",
            "description": "if the user wants to know about our hotels availiability with in 24 hours or in days weeks months",
            "parameters": {
                "type": "object",
                "properties": {
                    },
                "required": [],
                }
            },

{
            "name": "getRooms",
            "description": "it provides detailed information about the rooms found in one whole room",
            "parameters": {
                "type": "object",
                "properties": {
                    "room": {
                        "type" : "string",
                        "description": "the type of room we have in our hotel",
                        "enum": ["livingroom", "bedroom", "kitchen", "balcony"]
                        }
                    },
                "required": ["room"],
                }
            },


{
            "name": "safety",
            "description": "it provides information about the hotel's hazardous and safety precautions the user or customer must follow",
            "parameters": {
                "type": "object",
                "properties": {
                    },
                "required": [],
                }
            },
{
            "name": "getInfoCancel",
            "description": "this provides information about the hotel's cancellation policy about booking it provides general information",
            "parameters": {
                "type": "object",
                "properties": {
                    },
                "required": [],
                }
            },
{
            "name": "getPrivacy",
            "description": "this provides information the hotel extracts from the user all the necessary information the user must provides while staying in the hotel",
            "parameters": {
                "type": "object",
                "properties": {
                    },
                "required": [],
                }
            },
{
            "name": "getImages",
            "description": "Get the image of anything related to our hotel",
            "parameters": {
                "type": "object",
                "properties": {
                    },
                "required": [],
                }
            },
]
