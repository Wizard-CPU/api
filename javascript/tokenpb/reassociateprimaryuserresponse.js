// source: token.proto
/**
 * @fileoverview
 * @enhanceable
 * @suppress {messageConventions} JS Compiler reports an error if a variable or
 *     field starts with 'MSG_' and isn't a translatable message.
 * @public
 */
// GENERATED CODE -- DO NOT EDIT!

goog.provide('proto.tokenpb.ReassociatePrimaryUserResponse');

goog.require('jspb.BinaryReader');
goog.require('jspb.BinaryWriter');
goog.require('jspb.Message');
goog.require('proto.tokenpb.TokenBundle');

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
proto.tokenpb.ReassociatePrimaryUserResponse = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.tokenpb.ReassociatePrimaryUserResponse, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.tokenpb.ReassociatePrimaryUserResponse.displayName = 'proto.tokenpb.ReassociatePrimaryUserResponse';
}



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
proto.tokenpb.ReassociatePrimaryUserResponse.prototype.toObject = function(opt_includeInstance) {
  return proto.tokenpb.ReassociatePrimaryUserResponse.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.tokenpb.ReassociatePrimaryUserResponse} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.tokenpb.ReassociatePrimaryUserResponse.toObject = function(includeInstance, msg) {
  var f, obj = {
    data: (f = msg.getData()) && proto.tokenpb.TokenBundle.toObject(includeInstance, f)
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
 * @return {!proto.tokenpb.ReassociatePrimaryUserResponse}
 */
proto.tokenpb.ReassociatePrimaryUserResponse.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.tokenpb.ReassociatePrimaryUserResponse;
  return proto.tokenpb.ReassociatePrimaryUserResponse.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.tokenpb.ReassociatePrimaryUserResponse} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.tokenpb.ReassociatePrimaryUserResponse}
 */
proto.tokenpb.ReassociatePrimaryUserResponse.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.tokenpb.TokenBundle;
      reader.readMessage(value,proto.tokenpb.TokenBundle.deserializeBinaryFromReader);
      msg.setData(value);
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
proto.tokenpb.ReassociatePrimaryUserResponse.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.tokenpb.ReassociatePrimaryUserResponse.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.tokenpb.ReassociatePrimaryUserResponse} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.tokenpb.ReassociatePrimaryUserResponse.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getData();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.tokenpb.TokenBundle.serializeBinaryToWriter
    );
  }
};


/**
 * optional TokenBundle data = 1;
 * @return {?proto.tokenpb.TokenBundle}
 */
proto.tokenpb.ReassociatePrimaryUserResponse.prototype.getData = function() {
  return /** @type{?proto.tokenpb.TokenBundle} */ (
    jspb.Message.getWrapperField(this, proto.tokenpb.TokenBundle, 1));
};


/**
 * @param {?proto.tokenpb.TokenBundle|undefined} value
 * @return {!proto.tokenpb.ReassociatePrimaryUserResponse} returns this
*/
proto.tokenpb.ReassociatePrimaryUserResponse.prototype.setData = function(value) {
  return jspb.Message.setWrapperField(this, 1, value);
};


/**
 * Clears the message field making it undefined.
 * @return {!proto.tokenpb.ReassociatePrimaryUserResponse} returns this
 */
proto.tokenpb.ReassociatePrimaryUserResponse.prototype.clearData = function() {
  return this.setData(undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.tokenpb.ReassociatePrimaryUserResponse.prototype.hasData = function() {
  return jspb.Message.getField(this, 1) != null;
};


