// source: token.proto
/**
 * @fileoverview
 * @enhanceable
 * @suppress {messageConventions} JS Compiler reports an error if a variable or
 *     field starts with 'MSG_' and isn't a translatable message.
 * @public
 */
// GENERATED CODE -- DO NOT EDIT!

goog.provide('proto.tokenpb.RefreshTokenRequest');

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
proto.tokenpb.RefreshTokenRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.tokenpb.RefreshTokenRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.tokenpb.RefreshTokenRequest.displayName = 'proto.tokenpb.RefreshTokenRequest';
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
proto.tokenpb.RefreshTokenRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.tokenpb.RefreshTokenRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.tokenpb.RefreshTokenRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.tokenpb.RefreshTokenRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    refreshJwtTokens: jspb.Message.getBooleanFieldWithDefault(msg, 2, false),
    refreshStsTokens: jspb.Message.getBooleanFieldWithDefault(msg, 3, false),
    expirationMinutes: jspb.Message.getFieldWithDefault(msg, 4, 0)
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
 * @return {!proto.tokenpb.RefreshTokenRequest}
 */
proto.tokenpb.RefreshTokenRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.tokenpb.RefreshTokenRequest;
  return proto.tokenpb.RefreshTokenRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.tokenpb.RefreshTokenRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.tokenpb.RefreshTokenRequest}
 */
proto.tokenpb.RefreshTokenRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 2:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setRefreshJwtTokens(value);
      break;
    case 3:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setRefreshStsTokens(value);
      break;
    case 4:
      var value = /** @type {number} */ (reader.readUint32());
      msg.setExpirationMinutes(value);
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
proto.tokenpb.RefreshTokenRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.tokenpb.RefreshTokenRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.tokenpb.RefreshTokenRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.tokenpb.RefreshTokenRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getRefreshJwtTokens();
  if (f) {
    writer.writeBool(
      2,
      f
    );
  }
  f = message.getRefreshStsTokens();
  if (f) {
    writer.writeBool(
      3,
      f
    );
  }
  f = message.getExpirationMinutes();
  if (f !== 0) {
    writer.writeUint32(
      4,
      f
    );
  }
};


/**
 * optional bool refresh_jwt_tokens = 2;
 * @return {boolean}
 */
proto.tokenpb.RefreshTokenRequest.prototype.getRefreshJwtTokens = function() {
  return /** @type {boolean} */ (jspb.Message.getBooleanFieldWithDefault(this, 2, false));
};


/**
 * @param {boolean} value
 * @return {!proto.tokenpb.RefreshTokenRequest} returns this
 */
proto.tokenpb.RefreshTokenRequest.prototype.setRefreshJwtTokens = function(value) {
  return jspb.Message.setProto3BooleanField(this, 2, value);
};


/**
 * optional bool refresh_sts_tokens = 3;
 * @return {boolean}
 */
proto.tokenpb.RefreshTokenRequest.prototype.getRefreshStsTokens = function() {
  return /** @type {boolean} */ (jspb.Message.getBooleanFieldWithDefault(this, 3, false));
};


/**
 * @param {boolean} value
 * @return {!proto.tokenpb.RefreshTokenRequest} returns this
 */
proto.tokenpb.RefreshTokenRequest.prototype.setRefreshStsTokens = function(value) {
  return jspb.Message.setProto3BooleanField(this, 3, value);
};


/**
 * optional uint32 expiration_minutes = 4;
 * @return {number}
 */
proto.tokenpb.RefreshTokenRequest.prototype.getExpirationMinutes = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 4, 0));
};


/**
 * @param {number} value
 * @return {!proto.tokenpb.RefreshTokenRequest} returns this
 */
proto.tokenpb.RefreshTokenRequest.prototype.setExpirationMinutes = function(value) {
  return jspb.Message.setProto3IntField(this, 4, value);
};


