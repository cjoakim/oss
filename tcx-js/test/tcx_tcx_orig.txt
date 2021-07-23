
/*
Copyright 2015, Christopher Joakim <christopher.joakim@gmail.com>
 */

(function() {
  var pkg, tcx;

  tcx = require('../lib/tcx.js');

  pkg = require('../package.json');

  describe('tcx.Parser', function() {
    it('defines VERSION in both the code and package.json files', function() {
      var code_version, expected, pkg_version;
      expected = '0.1.3';
      code_version = tcx.Parser.VERSION;
      pkg_version = pkg.version;
      expect(code_version).toBe(expected);
      expect(code_version).toBe(expected);
      return expect(code_version).toBe(pkg_version);
    });
    it('defines constants related to its calculations, such as METERS_PER_MILE', function() {
      expect(tcx.Parser.FEET_PER_METER).toBe(3.280839895013123);
      return expect(tcx.Parser.METERS_PER_MILE).toBe(1609.344);
    });
    it('parses the Twin Cities Marathon sample data, quickly', function() {
      var activity, author, creator, elapsed_ms, finish_ms, parser, start_ms, t, trackpoints;
      start_ms = (new Date()).getTime();
      parser = new tcx.Parser();
      parser.parse_file('data/activity_twin_cities_marathon.tcx');
      finish_ms = (new Date()).getTime();
      elapsed_ms = finish_ms - start_ms;
      expect(elapsed_ms).toBeLessThan(500);
      expect(parser.root_tag).toBe('TrainingCenterDatabase');
      expect(parser.end_reached).toBe(true);
      activity = parser.activity;
      author = activity.author;
      creator = activity.creator;
      trackpoints = activity.trackpoints;
      expect(creator.name).toBe('Garmin Forerunner 620');
      expect(creator.unit_id).toBe('3875991210');
      expect(creator.product_id).toBe('1623');
      expect(creator.version_major).toBe('3');
      expect(creator.version_minor).toBe('0');
      expect(creator.build_major).toBe('0');
      expect(creator.build_minor).toBe('0');
      expect(author.name).toBe('Garmin Connect API');
      expect(author.version_major).toBe('14');
      expect(author.version_minor).toBe('10');
      expect(author.build_major).toBe('0');
      expect(author.build_minor).toBe('0');
      expect(author.lang).toBe('en');
      expect(author.part_number).toBe('006-D2449-00');
      expect(trackpoints.length).toBe(2256);
      t = trackpoints[0];
      expect(t.seq).toBe(1);
      expect(t.time).toBe('2014-10-05T13:07:53.000Z');
      expect(t.lat).toBe('44.97431952506304');
      expect(t.lng).toBe('-93.26310088858008');
      expect(t.alt_meters).toBe('257.0');
      expect(t.dist_meters).toBe('0.0');
      expect(t.hr_bpm).toBe('85');
      expect(t.run_cadence).toBe('89');
      t = trackpoints[2255];
      expect(t.seq).toBe(2256);
      expect(t.time).toBe('2014-10-05T17:22:17.000Z');
      expect(t.lat).toBe('44.95180849917233');
      expect(t.lng).toBe('-93.10493202880025');
      expect(t.alt_meters).toBe('260.0');
      expect(t.dist_meters).toBe('42635.44921875');
      expect(t.hr_bpm).toBe('161');
      return expect(t.run_cadence).toBe('77');
    });
    return it('optionally augments the parsed Trackpoints with calculated fields', function() {
      var elapsed_ms, finish_ms, opts, parser, start_ms, t, trackpoints;
      opts = {};
      opts.alt_feet = true;
      opts.dist_miles = true;
      opts.elapsed = true;
      start_ms = (new Date()).getTime();
      parser = new tcx.Parser(opts);
      parser.parse_file('data/activity_twin_cities_marathon.tcx');
      finish_ms = (new Date()).getTime();
      elapsed_ms = finish_ms - start_ms;
      expect(elapsed_ms).toBeLessThan(500);
      trackpoints = parser.activity.trackpoints;
      expect(trackpoints.length).toBe(2256);
      t = trackpoints[2255];
      expect(t.seq).toBe(2256);
      expect(t.time).toBe('2014-10-05T17:22:17.000Z');
      expect(t.lat).toBe('44.95180849917233');
      expect(t.lng).toBe('-93.10493202880025');
      expect(t.alt_meters).toBe('260.0');
      expect(t.dist_meters).toBe('42635.44921875');
      expect(t.hr_bpm).toBe('161');
      expect(t.run_cadence).toBe('77');
      expect(t.alt_feet).toBe(853.018372703412);
      expect(t.dist_miles).toBe(26.492439912628996);
      expect(t.elapsed_sec).toBe(15264);
      return expect(t.elapsed_hhmmss).toBe("04:14:24");
    });
  });

}).call(this);
