// source: jdocs.proto
/**
 * @fileoverview
 * @enhanceable
 * @suppress {messageConventions} JS Compiler reports an error if a variable or
 *     field starts with 'MSG_' and isn't a translatable message.
 * @public
 */
// GENERATED CODE -- DO NOT EDIT!

goog.provide('proto.jdocspb.ViewDocsResp');

goog.require('jspb.BinaryReader');
goog.require('jspb.BinaryWriter');
goog.require('jspb.Message');
goog.require('proto.jdocspb.ViewDoc');

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
proto.jdocspb.ViewDocsResp = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.jdocspb.ViewDocsResp.repeatedFields_, null);
};
goog.inherits(proto.jdocspb.ViewDocsResp, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.jdocspb.ViewDocsResp.displayName = 'proto.jdocspb.ViewDocsResp';
}

/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.jdocspb.ViewDocsResp.repeatedFields_ = [1];



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
proto.jdocspb.ViewDocsResp.prototype.toObject = function(opt_includeInstance) {
  return proto.jdocspb.ViewDocsResp.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.jdocspb.ViewDocsResp} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.jdocspb.ViewDocsResp.toObject = function(includeInstance, msg) {
  var f, obj = {
    docsList: jspb.Message.toObjectList(msg.getDocsList(),
    proto.jdocspb.ViewDoc.toObject, includeInstance)
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
 * @return {!proto.jdocspb.ViewDocsResp}
 */
proto.jdocspb.ViewDocsResp.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.jdocspb.ViewDocsResp;
  return proto.jdocspb.ViewDocsResp.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.jdocspb.ViewDocsResp} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.jdocspb.ViewDocsResp}
 */
proto.jdocspb.ViewDocsResp.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.jdocspb.ViewDoc;
      reader.readMessage(value,proto.jdocspb.ViewDoc.deserializeBinaryFromReader);
      msg.addDocs(value);
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
proto.jdocspb.ViewDocsResp.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.jdocspb.ViewDocsResp.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.jdocspb.ViewDocsResp} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.jdocspb.ViewDocsResp.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getDocsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      proto.jdocspb.ViewDoc.serializeBinaryToWriter
    );
  }
};


/**
 * repeated ViewDoc docs = 1;
 * @return {!Array<!proto.jdocspb.ViewDoc>}
 */
proto.jdocspb.ViewDocsResp.prototype.getDocsList = function() {
  return /** @type{!Array<!proto.jdocspb.ViewDoc>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.jdocspb.ViewDoc, 1));
};


/**
 * @param {!Array<!proto.jdocspb.ViewDoc>} value
 * @return {!proto.jdocspb.ViewDocsResp} returns this
*/
proto.jdocspb.ViewDocsResp.prototype.setDocsList = function(value) {
  return jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.jdocspb.ViewDoc=} opt_value
 * @param {number=} opt_index
 * @return {!proto.jdocspb.ViewDoc}
 */
proto.jdocspb.ViewDocsResp.prototype.addDocs = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.jdocspb.ViewDoc, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 * @return {!proto.jdocspb.ViewDocsResp} returns this
 */
proto.jdocspb.ViewDocsResp.prototype.clearDocsList = function() {
  return this.setDocsList([]);
};


