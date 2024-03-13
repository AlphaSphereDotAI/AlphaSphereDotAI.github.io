import 'package:animated_text_kit/animated_text_kit.dart';
import 'package:flutter/material.dart';
import 'package:flutter_svg/svg.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:url_launcher/link.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'AlphaSphere.AI',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(scaffoldBackgroundColor: const Color(0xFF000000)),
      home: Scaffold(
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              AnimatedTextKit(
                animatedTexts: [
                  TypewriterAnimatedText(
                    'AlphaSphere.AI',
                    textStyle: TextStyle(
                      fontWeight: FontWeight.bold,
                      color: Colors.white,
                      fontSize:
                          (MediaQuery.of(context).size.width * 0.1 < MediaQuery.of(context).size.height * 0.1) ? MediaQuery.of(context).size.width * 0.1 : MediaQuery.of(context).size.height * 0.1,
                      fontFamily: GoogleFonts.jetBrainsMono().fontFamily,
                    ),
                    speed: const Duration(milliseconds: 100),
                  ),
                ],
                repeatForever: false,
                isRepeatingAnimation: false,
              ),
              AnimatedTextKit(
                animatedTexts: [
                  TypewriterAnimatedText(
                    '',
                    textStyle: TextStyle(
                      color: Colors.white,
                      fontSize:
                          (MediaQuery.of(context).size.width * 0.04 < MediaQuery.of(context).size.height * 0.04) ? MediaQuery.of(context).size.width * 0.04 : MediaQuery.of(context).size.height * 0.04,
                      fontFamily: GoogleFonts.jetBrainsMono().fontFamily,
                    ),
                    speed: const Duration(milliseconds: 100),
                  ),
                ],
                repeatForever: false,
                isRepeatingAnimation: false,
              ),
              const SizedBox(
                height: 20,
              ),
              Link(
                target: LinkTarget.blank,
                uri: Uri.parse('MAILTO:AlphaSphereDotAI@googlegroups.com'),
                builder: (context, followLink) => OutlinedButton(
                  onPressed: followLink,
                  child: AnimatedTextKit(
                    onTap: followLink,
                    animatedTexts: [
                      TypewriterAnimatedText(
                        'AlphaSphereDotAI@googlegroups.com',
                        textStyle: TextStyle(
                          fontWeight: FontWeight.bold,
                          color: Colors.white,
                          fontSize: (MediaQuery.of(context).size.width * 0.03 < MediaQuery.of(context).size.height * 0.03)
                              ? MediaQuery.of(context).size.width * 0.03
                              : MediaQuery.of(context).size.height * 0.03,
                          fontFamily: GoogleFonts.jetBrainsMono().fontFamily,
                        ),
                        speed: const Duration(milliseconds: 100),
                      ),
                    ],
                    repeatForever: false,
                    isRepeatingAnimation: false,
                  ),
                ),
              ),
              const SizedBox(
                height: 20,
              ),
              const SizedBox(
                height: 20,
              ),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Link(
                    target: LinkTarget.blank,
                    uri: Uri.parse('https://GitHub.com/AlphaSphereDotAI'),
                    builder: (context, followLink) => IconButton(
                      color: Colors.white,
                      iconSize:
                          (MediaQuery.of(context).size.width * 0.05 < MediaQuery.of(context).size.height * 0.05) ? MediaQuery.of(context).size.width * 0.05 : MediaQuery.of(context).size.height * 0.05,
                      hoverColor: Colors.white24,
                      icon: const FaIcon(FontAwesomeIcons.github),
                      onPressed: followLink,
                    ),
                  ),
                  Link(
                    target: LinkTarget.blank,
                    uri: Uri.parse('https://Upwork.com/agencies/1665419267091288064'),
                    builder: (context, followLink) => IconButton(
                      color: Colors.white,
                      hoverColor: const Color(0xff14a800),
                      icon: SvgPicture.string(
                        '<svg xmlns="http://www.w3.org/2000/svg" height="16" width="14" viewBox="0 0 448 512"><path fill="#ffffff" d="M64 32C28.7 32 0 60.7 0 96V416c0 35.3 28.7 64 64 64H384c35.3 0 64-28.7 64-64V96c0-35.3-28.7-64-64-64H64zM270.8 274.3c5.2 8.4 23.6 29.9 51.5 29.9v0c25.2 0 44.9-20.2 44.9-49.7s-19.4-49.7-44.9-49.7s-44.9 16.7-51.5 69.5zm-26.7-41.8c7.3-30.5 32.7-60.1 78.2-60.1l0 0c45.1 0 80.9 35.2 80.9 82.2s-35.9 81.9-80.9 81.9c-.6 0-1.1 0-1.7 0c-.5 0-1.1 0-1.6 0h-.1c-14.5-.5-28.7-4.8-40.9-12.6c-4.7-2.8-9.1-6-13.4-9.5l-12.8 78.4H214.9l19.4-110.6c-20.8-29.1-31.6-62.4-36.2-79.7V255c0 48-30.5 81.5-74.2 81.5c-22 0-41-8-54.8-23.3c-13.4-14.8-20.8-35.5-20.8-58.3V176.8H84.5l-.3 78.2c0 28.4 14.5 49.3 39.8 49.3s38.2-20.9 38.2-49.3V176.8h62.8c4.8 19.3 10.9 40.1 19.2 55.6z"/></svg>',
                        height: (MediaQuery.of(context).size.width * 0.05 < MediaQuery.of(context).size.height * 0.05)
                            ? MediaQuery.of(context).size.width * 0.05
                            : MediaQuery.of(context).size.height * 0.05,
                      ),
                      onPressed: followLink,
                    ),
                  ),
                  Link(
                    target: LinkTarget.blank,
                    uri: Uri.parse('https://Linkedin.com/company/alphaspheredotai'),
                    builder: (context, followLink) => IconButton(
                      color: Colors.white,
                      hoverColor: const Color(0xff14a800),
                      icon: const FaIcon(FontAwesomeIcons.linkedin),
                      onPressed: followLink,
                    ),
                  ),
                  Link(
                    target: LinkTarget.blank,
                    uri: Uri.parse('https://www.kaggle.com/organizations/AlphaSphereDotAI'),
                    builder: (context, followLink) => IconButton(
                      color: Colors.white,
                      hoverColor: const Color(0xff14a800),
                      icon: const FaIcon(FontAwesomeIcons.kaggle),
                      onPressed: followLink,
                    ),
                  )
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}
