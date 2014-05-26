## base.mako
<!DOCTYPE html>
<%block name="html_tag">
<html class="" lang="en">
</%block>
<head>
<%block name="head"><%include file="cuorewebpage:templates/head.mako"/></%block>
</head>

<%block name="body_tag"><body></%block>${next.body()}</body>
</html>

