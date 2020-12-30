// source: jdocs.proto
/**
 * @fileoverview
 * @enhanceable
 * @suppress {messageConventions} JS Compiler reports an error if a variable or
 *     field starts with 'MSG_' and isn't a translatable message.
 * @public
 */
// GENERATED CODE -- DO NOT EDIT!

goog.provide('proto.jdocspb.ReadDocsReq');
goog.provide('proto.jdocspb.ReadDocsReq.Item');

goog.require('jspb.BinaryReader');
goog.require('jspb.BinaryWriter');
goog.require('jspb.Message');

/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.jdocspb.ReadDocsReq = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.jdocspb.ReadDocsReq.repeatedFields_, null);
};
goog.inherits(proto.jdocspb.ReadDocsReq, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.jdocspb.ReadDocsReq.displayName = 'proto.jdocspb.ReadDocsReq';
}
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.jdocspb.ReadDocsReq.Item = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.jdocspb.ReadDocsReq.Item, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.jdocspb.ReadDocsReq.Item.displayName = 'proto.jdocspb.ReadDocsReq.Item';
}

/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.jdocspb.ReadDocsReq.repeatedFields_ = [3];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.jdocspb.ReadDocsReq.prototype.toObject = function(opt_includeInstance) {
  return proto.jdocspb.ReadDocsReq.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.jdocspb.ReadDocsReq} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.jdocspb.ReadDocsReq.toObject = function(includeInstance, msg) {
  var f, obj = {
    userId: jspb.Message.getFieldWithDefault(msg, 1, ""),
    thing: jspb.Message.getFieldWithDefault(msg, 2, ""),
    itemsList: jspb.Message.toObjectList(msg.getItemsList(),
    proto.jdocspb.ReadDocsReq.Item.toObject, includeInstance)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.jdocspb.ReadDocsReq}
 */
proto.jdocspb.ReadDocsReq.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.jdocspb.ReadDocsReq;
  return proto.jdocspb.ReadDocsReq.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.jdocspb.ReadDocsReq} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.jdocspb.ReadDocsReq}
 */
proto.jdocspb.ReadDocsReq.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {string} */ (reader.readString());
      msg.setUserId(value);
      break;
    case 2:
      var value = /** @type {string} */ (reader.readString());
      msg.setThing(value);
      break;
    case 3:
      var value = new proto.jdocspb.ReadDocsReq.Item;
      reader.readMessage(value,proto.jdocspb.ReadDocsReq.Item.deserializeBinaryFromReader);
      msg.addItems(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.jdocspb.ReadDocsReq.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.jdocspb.ReadDocsReq.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.jdocspb.ReadDocsReq} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.jdocspb.ReadDocsReq.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getUserId();
  if (f.length > 0) {
    writer.writeString(
      1,
      f
    );
  }
  f = message.getThing();
  if (f.length > 0) {
    writer.writeString(
      2,
      f
    );
  }
  f = message.getItemsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      3,
      f,
      proto.jdocspb.ReadDocsReq.Item.serializeBinaryToWriter
    );
  }
};





if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.jdocspb.ReadDocsReq.Item.prototype.toObject = function(opt_includeInstance) {
  return proto.jdocspb.ReadDocsReq.Item.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.jdocspb.ReadDocsReq.Item} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.jdocspb.ReadDocsReq.Item.toObject = function(includeInstance, msg) {
  var f, obj = {
    docName: jspb.Message.getFieldWithDefault(msg, 1, ""),
    myDocVersion: jspb.Message.getFieldWithDefault(msg, 2, 0)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.jdocspb.ReadDocsReq.Item}
 */
proto.jdocspb.ReadDocsReq.Item.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.jdocspb.ReadDocsReq.Item;
  return proto.jdocspb.ReadDocsReq.Item.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.jdocspb.ReadDocsReq.Item} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.jdocspb.ReadDocsReq.Item}
 */
proto.jdocspb.ReadDocsReq.Item.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {string} */ (reader.readString());
      msg.setDocName(value);
      break;
    case 2:
      var value = /** @type {number} */ (reader.readUint64());
      msg.setMyDocVersion(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.jdocspb.ReadDocsReq.Item.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.jdocspb.ReadDocsReq.Item.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.jdocspb.ReadDocsReq.Item} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.jdocspb.ReadDocsReq.Item.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getDocName();
  if (f.length > 0) {
    writer.writeString(
      1,
      f
    );
  }
  f = message.getMyDocVersion();
  if (f !== 0) {
    writer.writeUint64(
      2,
      f
    );
  }
};


/**
 * optional string doc_name = 1;
 * @return {string}
 */
proto.jdocspb.ReadDocsReq.Item.prototype.getDocName = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 1, ""));
};


/**
 * @param {string} value
 * @return {!proto.jdocspb.ReadDocsReq.Item} returns this
 */
proto.jdocspb.ReadDocsReq.Item.prototype.setDocName = function(value) {
  return jspb.Message.setProto3StringField(this, 1, value);
};


/**
 * optional uint64 my_doc_version = 2;
 * @return {number}
 */
proto.jdocspb.ReadDocsReq.Item.prototype.getMyDocVersion = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 2, 0));
};


/**
 * @param {number} value
 * @return {!proto.jdocspb.ReadDocsReq.Item} returns this
 */
proto.jdocspb.ReadDocsReq.Item.prototype.setMyDocVersion = function(value) {
  return jspb.Message.setProto3IntField(this, 2, value);
};


/**
 * optional string user_id = 1;
 * @return {string}
 */
proto.jdocspb.ReadDocsReq.prototype.getUserId = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 1, ""));
};


/**
 * @param {string} value
 * @return {!proto.jdocspb.ReadDocsReq} returns this
 */
proto.jdocspb.ReadDocsReq.prototype.setUserId = function(value) {
  return jspb.Message.setProto3StringField(this, 1, value);
};


/**
 * optional string thing = 2;
 * @return {string}
 */
proto.jdocspb.ReadDocsReq.prototype.getThing = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 2, ""));
};


/**
 * @param {string} value
 * @return {!proto.jdocspb.ReadDocsReq} returns this
 */
proto.jdocspb.ReadDocsReq.prototype.setThing = function(value) {
  return jspb.Message.setProto3StringField(this, 2, value);
};


/**
 * repeated Item items = 3;
 * @return {!Array<!proto.jdocspb.ReadDocsReq.Item>}
 */
proto.jdocspb.ReadDocsReq.prototype.getItemsList = function() {
  return /** @type{!Array<!proto.jdocspb.ReadDocsReq.Item>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.jdocspb.ReadDocsReq.Item, 3));
};


/**
 * @param {!Array<!proto.jdocspb.ReadDocsReq.Item>} value
 * @return {!proto.jdocspb.ReadDocsReq} returns this
*/
proto.jdocspb.ReadDocsReq.prototype.setItemsList = function(value) {
  return jspb.Message.setRepeatedWrapperField(this, 3, value);
};


/**
 * @param {!proto.jdocspb.ReadDocsReq.Item=} opt_value
 * @param {number=} opt_index
 * @return {!proto.jdocspb.ReadDocsReq.Item}
 */
proto.jdocspb.ReadDocsReq.prototype.addItems = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 3, opt_value, proto.jdocspb.ReadDocsReq.Item, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 * @return {!proto.jdocspb.ReadDocsReq} returns this
 */
proto.jdocspb.ReadDocsReq.prototype.clearItemsList = function() {
  return this.setItemsList([]);
};


